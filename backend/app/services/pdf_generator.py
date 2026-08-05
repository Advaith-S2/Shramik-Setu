"""
services/pdf_generator.py — M-08: Employment Passport PDF
Uses ReportLab (not Puppeteer/WeasyPrint per AGENTS.md §2).
Requires Devanagari font support for Hindi/Marathi.
Stub — implement in Day 8.
"""


def generate_passport_pdf(worker_data: dict) -> bytes:
    """
    Generate Employment Passport PDF for a worker.
    Returns raw PDF bytes.

    Args:
        worker_data: Dict containing worker profile, employment history,
                     attendance summary, wage records, payment history.

    Font note (Day 8): Use NotoSansDevanagari-Regular.ttf for HI/MR content.
    Download from Google Fonts; register with ReportLab's pdfmetrics.
    Rate limit: 1 request per 30 seconds per user (PRD §11.5).
    """
    # TODO (M-08 Day 8): build PDF with ReportLab canvas
    raise NotImplementedError("pdf_generator — implement in Day 8 (M-08)")
