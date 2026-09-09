"""Reference-specific read-only extraction probe, not a universal layout parser.

Run: python3 validation/reading_order_probe.py PRIVATE_CV.pdf
Only non-personal aggregate observations are printed.
"""
import json
import sys
import pdfplumber


def intrusion(text):
    block = text.split('BILDUNG', 1)[1].split('PRAXIS & BERUFSERFAHRUNG', 1)[0]
    return [s for s in ['PERSÖNLICHES', 'ADRESSE', 'E-MAIL', 'TELEFON', 'GEBOREN', 'IT-KENNTNISSE'] if s in block]


if __name__ == '__main__':
    with pdfplumber.open(sys.argv[1]) as doc:
        page = doc.pages[0]
        main = page.crop((175, 0, page.width, page.height))
        sidebar = page.crop((0, 0, 175, page.height))
        print(json.dumps({
            'raw_geometry_extraction_sidebar_headings_inside_education': len(intrusion(page.extract_text())),
            'column_scoped_extraction_sidebar_headings_inside_education': len(intrusion(main.extract_text())),
            'all_character_objects_preserved': len(page.chars) == len(main.chars) + len(sidebar.chars),
            'split_x_points': 175,
            'scope': 'reference-specific extraction probe, no PDF modification or ATS guarantee',
        }, indent=2))
