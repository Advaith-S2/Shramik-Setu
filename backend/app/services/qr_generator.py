"""
services/qr_generator.py — M-04: QR Contract Generation
Uses `qrcode` Python library (not client-side JS). Returns PNG bytes.
Stub — implement in Day 4.
"""
import io
import uuid


def generate_qr_token() -> str:
    """Generate a unique, random QR token (UUID4 string)."""
    return str(uuid.uuid4())


def generate_qr_image(data: str) -> bytes:
    """
    Generate a QR code PNG image encoding `data`.
    Returns raw PNG bytes to be stored in Supabase Storage or returned inline.

    Args:
        data: The URL or token string to encode (e.g. acceptance URL).

    Raises:
        ImportError if qrcode/Pillow not installed.
    """
    # TODO (M-04 Day 4): uncomment when implementing
    # import qrcode
    # from PIL import Image
    # qr = qrcode.QRCode(version=1, box_size=10, border=4)
    # qr.add_data(data)
    # qr.make(fit=True)
    # img = qr.make_image(fill_color="black", back_color="white")
    # buf = io.BytesIO()
    # img.save(buf, format="PNG")
    # return buf.getvalue()
    raise NotImplementedError("qr_generator — implement in Day 4 (M-04)")
