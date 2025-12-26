"""Data classes representing key entities."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


def now_iso() -> str:
    return datetime.utcnow().isoformat()


@dataclass
class User:
    full_name: str
    username: str
    password_hash: str
    role: str
    phone: str
    national_id: str
    created_at: str = now_iso()


@dataclass
class Exercise:
    name: str
    description: str
    body_part: str
    equipment: str
    difficulty: str
    video_path: str
    created_at: str = now_iso()


@dataclass
class Plan:
    user_id: int
    plan_date: str
    plan_type: str
    created_at: str = now_iso()


@dataclass
class PlanItem:
    plan_id: int
    exercise_id: int
    sets: int
    reps: int
    weight: float | None = None
    rest_seconds: int | None = None


@dataclass
class ProgressLog:
    user_id: int
    log_date: str
    weight: float
    chest: float | None = None
    waist: float | None = None
    arms: float | None = None
    thighs: float | None = None
    notes: str | None = None
