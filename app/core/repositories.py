"""Repositories encapsulating database CRUD logic."""
from __future__ import annotations

from datetime import datetime
from typing import Iterable

from .database import DB
from .models import Exercise, Plan, PlanItem, ProgressLog, User


class UsersRepository:
    def create(self, user: User) -> int:
        cur = DB.cursor()
        cur.execute(
            "INSERT INTO users (full_name, username, password_hash, role, phone, national_id, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                user.full_name,
                user.username,
                user.password_hash,
                user.role,
                user.phone,
                user.national_id,
                user.created_at,
            ),
        )
        DB.commit()
        return cur.lastrowid

    def update(self, user_id: int, data: dict) -> None:
        fields = ", ".join(f"{k}=?" for k in data.keys())
        values = list(data.values()) + [user_id]
        DB.cursor().execute(f"UPDATE users SET {fields} WHERE id=?", values)
        DB.commit()

    def delete(self, user_id: int) -> None:
        DB.cursor().execute("DELETE FROM users WHERE id=?", (user_id,))
        DB.commit()

    def all(self) -> Iterable[dict]:
        cur = DB.cursor()
        cur.execute("SELECT * FROM users ORDER BY created_at DESC")
        return cur.fetchall()

    def search(self, query: str) -> Iterable[dict]:
        q = f"%{query}%"
        cur = DB.cursor()
        cur.execute(
            "SELECT * FROM users WHERE full_name LIKE ? OR phone LIKE ? OR national_id LIKE ? OR username LIKE ?",
            (q, q, q, q),
        )
        return cur.fetchall()

    def get_by_username(self, username: str):
        cur = DB.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        return cur.fetchone()


class ExercisesRepository:
    def create(self, exercise: Exercise) -> int:
        cur = DB.cursor()
        cur.execute(
            "INSERT INTO exercises (name, description, body_part, equipment, difficulty, video_path, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                exercise.name,
                exercise.description,
                exercise.body_part,
                exercise.equipment,
                exercise.difficulty,
                exercise.video_path,
                exercise.created_at,
            ),
        )
        DB.commit()
        return cur.lastrowid

    def delete(self, exercise_id: int) -> None:
        DB.cursor().execute("DELETE FROM exercises WHERE id=?", (exercise_id,))
        DB.commit()

    def all(self) -> Iterable[dict]:
        cur = DB.cursor()
        cur.execute("SELECT * FROM exercises ORDER BY created_at DESC")
        return cur.fetchall()


class PlansRepository:
    def create(self, plan: Plan) -> int:
        cur = DB.cursor()
        cur.execute(
            "INSERT INTO plans (user_id, plan_date, plan_type, created_at) VALUES (?, ?, ?, ?)",
            (plan.user_id, plan.plan_date, plan.plan_type, plan.created_at),
        )
        DB.commit()
        return cur.lastrowid

    def add_items(self, items: list[PlanItem]) -> None:
        cur = DB.cursor()
        cur.executemany(
            "INSERT INTO plan_items (plan_id, exercise_id, sets, reps, weight, rest_seconds) VALUES (?, ?, ?, ?, ?, ?)",
            [(i.plan_id, i.exercise_id, i.sets, i.reps, i.weight, i.rest_seconds) for i in items],
        )
        DB.commit()

    def plans_for_user(self, user_id: int):
        cur = DB.cursor()
        cur.execute(
            """
            SELECT p.*, group_concat(e.name, '\n') AS exercise_names
            FROM plans p
            LEFT JOIN plan_items pi ON pi.plan_id = p.id
            LEFT JOIN exercises e ON e.id = pi.exercise_id
            WHERE p.user_id=?
            GROUP BY p.id
            ORDER BY plan_date DESC
            """,
            (user_id,),
        )
        return cur.fetchall()

    def plan_items_for_date(self, user_id: int, plan_date: str):
        cur = DB.cursor()
        cur.execute(
            """
            SELECT pi.*, e.name, e.video_path, e.description
            FROM plans p
            JOIN plan_items pi ON pi.plan_id = p.id
            JOIN exercises e ON e.id = pi.exercise_id
            WHERE p.user_id=? AND p.plan_date=?
            ORDER BY pi.id
            """,
            (user_id, plan_date),
        )
        return cur.fetchall()


class ProgressRepository:
    def log(self, entry: ProgressLog) -> int:
        cur = DB.cursor()
        cur.execute(
            "INSERT INTO progress_logs (user_id, log_date, weight, chest, waist, arms, thighs, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                entry.user_id,
                entry.log_date,
                entry.weight,
                entry.chest,
                entry.waist,
                entry.arms,
                entry.thighs,
                entry.notes,
            ),
        )
        DB.commit()
        return cur.lastrowid

    def logs_for_user(self, user_id: int):
        cur = DB.cursor()
        cur.execute(
            "SELECT * FROM progress_logs WHERE user_id=? ORDER BY log_date DESC",
            (user_id,),
        )
        return cur.fetchall()


class SettingsRepository:
    def get_theme(self) -> str:
        cur = DB.cursor()
        cur.execute("SELECT theme FROM settings WHERE id=?", (CONFIG.settings_id,))
        row = cur.fetchone()
        return row[0] if row else "light"

    def set_theme(self, theme: str) -> None:
        DB.cursor().execute(
            "INSERT INTO settings (id, theme) VALUES (?, ?) ON CONFLICT(id) DO UPDATE SET theme=excluded.theme",
            (CONFIG.settings_id, theme),
        )
        DB.commit()


USERS = UsersRepository()
EXERCISES = ExercisesRepository()
PLANS = PlansRepository()
PROGRESS = ProgressRepository()
SETTINGS = SettingsRepository()
