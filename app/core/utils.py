"""Misc utilities."""
from __future__ import annotations

from datetime import datetime


def today() -> str:
    return datetime.utcnow().date().isoformat()
