"""Read-only private PDF audit. Output contains metrics only, no text/paths/hashes.

Experiment dependencies: PyMuPDF and pdfplumber. Not a renderer/stack choice.
Run with two private paths: python3 validation/audit_pdf.py LETTER.pdf CV.pdf
"""
import json
import sys
import fitz
import pdfplumber


def audit(path, alias):
    rows = []
    with fitz.open(path) as doc, pdfplumber.open(path) as second:
        for i, page in enumerate(doc):
            spans = [s for b in page.get_text('dict')['blocks'] if b['type'] == 0
                     for line in b['lines'] for s in line['spans']]
            rows.append({
                'page': i + 1,
                'a4_within_one_point': abs(page.rect.width - 595.276) < 1 and abs(page.rect.height - 841.89) < 1,
                'native_text_present': bool(spans),
                'pymupdf_characters': len(page.get_text()),
                'pdfplumber_characters': len(second.pages[i].extract_text() or ''),
                'text_spans_outside_page': sum(not page.rect.contains(fitz.Rect(s['bbox'])) for s in spans),
                'image_count': len(page.get_images()),
                'all_referenced_fonts_embedded': all(bool(doc.extract_font(f[0])[3]) for f in page.get_fonts()),
            })
    return {'artifact': alias, 'pages': rows}


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('Supply two private PDF paths; do not put private inputs in the repository.')
    print(json.dumps([audit(sys.argv[1], 'reference-letter'), audit(sys.argv[2], 'reference-cv')], indent=2))
