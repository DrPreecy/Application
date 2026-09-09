"""Disposable stdlib validation model; neither product code nor a stack decision.

Run: python3 validation/experiment.py
The oracle is explicit expected sets derived from F-001–005 and F-012–013.
"""
import json
from pathlib import Path


def ready(tasks, known):
    return sorted(k for k, deps in tasks.items() if set(deps) <= set(known))


def affected(graph, changed):
    reached = set(changed)
    while True:
        new = {k for k, deps in graph.items() if set(deps) & reached} - reached
        if not new:
            return sorted(reached - set(changed))
        reached |= new


def run():
    cases = json.loads(Path(__file__).with_name('cases.json').read_text())
    results = []
    for case in cases:
        if case['kind'] == 'readiness':
            actual = ready(case['graph'], case['input'])
            # Historical over-blocking: one missing dependency freezes everything.
            mutant = actual if len(actual) == len(case['graph']) else []
        else:
            actual = affected(case['graph'], case['input'])
            # Historical broad invalidation: any change invalidates every artifact.
            mutant = sorted(case['graph']) if case['input'] else []
        expected = sorted(case['expected'])
        results.append(dict(id=case['id'], expected=expected, actual=actual,
                            passed=actual == expected,
                            historical_mutant_rejected=mutant != expected))
    report = {'scope': 'synthetic dependency-model experiment only', 'results': results,
              'passed': sum(r['passed'] for r in results), 'total': len(results),
              'historical_mutants_rejected': sum(r['historical_mutant_rejected'] for r in results)}
    print(json.dumps(report, indent=2))
    assert all(r['passed'] for r in results)
    assert report['historical_mutants_rejected'] >= 5


if __name__ == '__main__':
    run()
