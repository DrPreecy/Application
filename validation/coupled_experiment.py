"""Disposable synthetic control model. No private source text or applicant facts.

Exercises version checks, locked-content scope and file-backed retry at bounded scale.
The temporary JSON checkpoint is experiment apparatus, not selected production storage.
"""
import copy
import json
import tempfile
from pathlib import Path
from experiment import affected


GRAPH = {
    'fit': ['rating-input'],
    'eligibility': ['qualification'],
    'positioning': ['career-fact'],
    'letter-argument': ['positioning'],
    'cv-career': ['career-fact'],
    'cv-language': ['language-claim'],
    'package': ['letter-argument', 'cv-career', 'cv-language', 'eligibility'],
}


def evaluate(s):
    reasons = []
    if s['unverified_claims']:
        reasons.append('claim_evidence_missing')
    if s['source_conflict']:
        reasons.append('source_conflict')
    if s['reading_order'] != 'checked':
        reasons.append('reading_order_review')
    if s['letter_positioning'] != s['cv_positioning']:
        reasons.append('positioning_mismatch')
    if s['letter_identity'] != s['cv_identity']:
        reasons.append('document_identity_mismatch')
    if s['stale']:
        reasons.append('dependent_results_stale')
    return {'package_review_ready': not reasons, 'reasons': reasons,
            'fit': s['fit'], 'eligibility': s['eligibility'],
            'submission_ready': not reasons and s['eligibility'] == 'confirmed' and s['user_release'],
            'allowed_work': ['inspect_sources', 'inspect_documents', 'prepare_unaffected_sections']}


def commit_candidate(path, expected_revision, operation, patch, allowed_sections, fail_after_save=False):
    state = json.loads(path.read_text())
    if state['schema'] != 1:
        raise ValueError('incompatible_schema')
    if operation in state['operations']:
        if state['operations'][operation]['patch'] != patch:
            raise ValueError('operation_payload_conflict')
        return state, 'already_committed'
    if state['revision'] != expected_revision:
        raise ValueError('stale_revision')
    if set(patch) - set(allowed_sections):
        raise ValueError('outside_authorized_scope')
    if set(patch) - set(state['sections']):
        raise ValueError('unknown_section')
    state['sections'].update(patch)
    state['revision'] += 1
    state['operations'][operation] = {'patch': patch, 'revision': state['revision']}
    staged = path.with_suffix('.staged')
    staged.write_text(json.dumps(state, sort_keys=True))
    staged.replace(path)
    if fail_after_save:
        raise RuntimeError('simulated_lost_acknowledgement')
    return state, 'committed'


def run():
    checks = []

    def check(name, observed, expected):
        checks.append({'id': name, 'observed': observed, 'expected': expected, 'pass': observed == expected})

    base = {'unverified_claims': ['claim-X'], 'source_conflict': True,
            'reading_order': 'disputed', 'letter_positioning': 1, 'cv_positioning': 1,
            'letter_identity': 1, 'cv_identity': 1, 'stale': [],
            'fit': 'promising-synthetic', 'eligibility': 'unknown', 'user_release': False}
    out = evaluate(base)
    check('C01-coupled-hold', out['reasons'], ['claim_evidence_missing', 'source_conflict', 'reading_order_review'])
    check('C02-no-global-freeze', out['allowed_work'], ['inspect_sources', 'inspect_documents', 'prepare_unaffected_sections'])
    check('C03-fit-not-eligibility', [out['fit'], out['eligibility'], out['submission_ready']], ['promising-synthetic', 'unknown', False])
    corrected = copy.deepcopy(base)
    corrected['unverified_claims'] = []
    check('C04-local-evidence-fix-not-global-pass', evaluate(corrected)['reasons'], ['source_conflict', 'reading_order_review'])
    check('C05-local-language-change', affected(GRAPH, ['language-claim']), ['cv-language', 'package'])
    check('C06-coupled-upstream-change', affected(GRAPH, ['career-fact', 'language-claim']), ['cv-career', 'cv-language', 'letter-argument', 'package', 'positioning'])
    corrected.update(source_conflict=False, reading_order='checked')
    check('C07-review-not-submission', [evaluate(corrected)['package_review_ready'], evaluate(corrected)['submission_ready']], [True, False])
    corrected['cv_positioning'] = 2
    corrected['cv_identity'] = 2
    check('C08-package-versions', evaluate(corrected)['reasons'], ['positioning_mismatch', 'document_identity_mismatch'])

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / 'checkpoint.json'
        original = {'schema': 1, 'revision': 1, 'operations': {},
                    'truth': {'fact-A': 'user-owned'},
                    'sections': {'locked-A': 'approved synthetic text', 'editable-B': 'candidate v1'}}
        path.write_text(json.dumps(original))
        try:
            commit_candidate(path, 1, 'op-1', {'editable-B': 'candidate v2'}, ['editable-B'], True)
        except RuntimeError:
            pass
        resumed, status = commit_candidate(path, 1, 'op-1', {'editable-B': 'candidate v2'}, ['editable-B'])
        check('C09-retry-after-lost-ack', [status, len(resumed['operations']), resumed['revision']], ['already_committed', 1, 2])
        check('C10-truth-and-lock-preserved', [resumed['truth'], resumed['sections']['locked-A']], [original['truth'], original['sections']['locked-A']])
        for name, revision, op, patch, allowed, error in [
            ('C11-outdated-worker', 1, 'op-2', {'editable-B': 'old result'}, ['editable-B'], 'stale_revision'),
            ('C12-unrelated-rewrite', 2, 'op-3', {'locked-A': 'rewrite'}, ['editable-B'], 'outside_authorized_scope'),
            ('C13-reused-operation-new-payload', 2, 'op-1', {'editable-B': 'different result'}, ['editable-B'], 'operation_payload_conflict'),
        ]:
            before = path.read_bytes()
            observed = 'not_rejected'
            try:
                commit_candidate(path, revision, op, patch, allowed)
            except ValueError as exc:
                observed = str(exc)
            check(name, [observed, path.read_bytes() == before], [error, True])
        changed = json.loads(path.read_text()); changed['schema'] = 2
        path.write_text(json.dumps(changed))
        try:
            commit_candidate(path, 2, 'op-4', {'editable-B': 'new'}, ['editable-B'])
            observed = 'not_rejected'
        except ValueError as exc:
            observed = str(exc)
        check('C14-schema-stop', observed, 'incompatible_schema')

    # Deliberately faulty decisions must disagree with the independent expected values above.
    # Explicit oracles avoid treating a failed experiment as a mutant success.
    mutants = {
        'ignore-package-holds': True != out['package_review_ready'],
        'freeze-all-work': [] != out['allowed_work'],
        'local-fix-clears-all': [] != ['source_conflict', 'reading_order_review'],
        'invalidate-everything': sorted(GRAPH) != affected(GRAPH, ['language-claim']),
        'repeat-commit-on-retry': 2 != len(resumed['operations']),
    }
    report = {'scope': 'synthetic controls informed by private reference review; not production proof',
              'checks': checks, 'passed': sum(c['pass'] for c in checks), 'total': len(checks),
              'mutants_rejected': mutants}
    print(json.dumps(report, indent=2))
    assert all(c['pass'] for c in checks)
    assert all(mutants.values())


if __name__ == '__main__':
    run()
