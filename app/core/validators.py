"""Input validation helpers."""
from __future__ import annotations

import re


def is_valid_phone(phone: str) -> bool:
    return bool(re.fullmatch(r"\d{11}", phone or ""))


def is_valid_national_id(national_id: str) -> bool:
    """Validate Iranian national code."""
    if not re.fullmatch(r"\d{10}", national_id or ""):
        return False
    digits = list(map(int, national_id))
    checksum = digits[-1]
    s = sum(d * (10 - i) for i, d in enumerate(digits[:9], start=1))
    r = s % 11
    return (r < 2 and checksum == r) or (r >= 2 and checksum + r == 11)


def require_fields(data: dict, fields: list[str]) -> tuple[bool, str]:
    missing = [f for f in fields if not data.get(f)]
    if missing:
        return False, f"فیلدهای الزامی: {', '.join(missing)}"
    return True, ""
