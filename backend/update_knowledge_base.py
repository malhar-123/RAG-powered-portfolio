"""
Scans the /resumes folder for PDFs, extracts their text,
and appends them to knowledge_base.py as new DOCUMENTS entries.
Run via GitHub Actions whenever resumes are pushed.
"""

import os
import re
import sys

try:
    import pypdf
except ImportError:
    print("pypdf not installed. Run: pip install pypdf")
    sys.exit(1)

RESUMES_DIR = os.path.join(os.path.dirname(__file__), '..', 'resumes')
KB_FILE = os.path.join(os.path.dirname(__file__), 'knowledge_base.py')

RESUME_MARKER = "# == AUTO-GENERATED RESUME DOCUMENTS ============================================="


def clean_text(text):
    """Remove or replace characters that would break Python string syntax."""
    # Replace triple quotes to avoid breaking the string delimiter
    text = text.replace('"""', "'''")
    # Replace problematic unicode characters
    replacements = {
        '—': '-',   # em dash
        '–': '-',   # en dash
        '‘': "'",   # left single quote
        '’': "'",   # right single quote
        '“': '"',   # left double quote
        '”': '"',   # right double quote
        '•': '-',   # bullet
        ' ': ' ',   # non-breaking space
        '�': '',    # replacement character
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    # Remove any remaining non-ASCII characters that could cause issues
    text = text.encode('ascii', errors='ignore').decode('ascii')
    return text


def extract_text_from_pdf(pdf_path):
    text = []
    with open(pdf_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text.append(t.strip())
    return clean_text("\n".join(text))


def parse_filename(filename):
    """Parse 'Malhar Gudekar Data Engineer Acme Corp.pdf' into role/company info."""
    name = os.path.splitext(filename)[0]
    return name


def main():
    pdf_files = [f for f in os.listdir(RESUMES_DIR) if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("No PDFs found in /resumes — nothing to update.")
        return

    resume_docs = []
    for pdf_file in sorted(pdf_files):
        pdf_path = os.path.join(RESUMES_DIR, pdf_file)
        label = parse_filename(pdf_file)
        print(f"Extracting: {pdf_file}")
        try:
            text = extract_text_from_pdf(pdf_path)
            if text.strip():
                doc = f"""TAILORED RESUME - {label}
{text}"""
                resume_docs.append(doc)
            else:
                print(f"  Warning: No text extracted from {pdf_file}")
        except Exception as e:
            print(f"  Error processing {pdf_file}: {e}")

    if not resume_docs:
        print("No text could be extracted from any PDF.")
        return

    # Read current knowledge_base.py
    with open(KB_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any previously auto-generated resume section
    if RESUME_MARKER in content:
        content = content[:content.index(RESUME_MARKER)].rstrip()

    # Remove the closing bracket if present
    content = content.rstrip()
    if content.endswith(']'):
        content = content[:-1].rstrip()

    # Build new resume entries
    new_entries = f"\n\n    {RESUME_MARKER}\n"
    for doc in resume_docs:
        escaped = doc.replace('"""', "'''")
        new_entries += f'\n    """{escaped}""",\n'

    new_entries += "\n]"

    # Write back
    with open(KB_FILE, 'w', encoding='utf-8') as f:
        f.write(content + new_entries)

    print(f"\nDone! Added {len(resume_docs)} resume(s) to knowledge_base.py")


if __name__ == '__main__':
    main()
