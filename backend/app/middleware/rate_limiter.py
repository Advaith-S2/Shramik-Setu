"""
middleware/rate_limiter.py — Rate limiting middleware
Stub — implement per PRD §11.5 limits.
"""
# TODO: Implement rate limiting per PRD §11.5:
#   - Auth endpoints: 5 req/min per IP
#   - Attendance marking: 5 attempts/day per worker
#   - PDF generation: 1 req/30s per user
#   - General API: 100 req/min per user
# Consider: slowapi (starlette-based) or simple in-memory counter for MVP
