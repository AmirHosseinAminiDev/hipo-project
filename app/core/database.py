"""SQLite database management."""
from __future__ import annotations

import sqlite3
from datetime import datetime

from .config import CONFIG
from .paths import PATHS
from .security import hash_password


class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(PATHS.db_path)
        self.connection.row_factory = sqlite3.Row
        self.ensure_schema()

    def ensure_schema(self) -> None:
        cur = self.connection.cursor()
        cur.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,
                username TEXT UNIQUE,
                password_hash TEXT,
                role TEXT,
                phone TEXT,
                national_id TEXT UNIQUE,
                created_at TEXT
            );

            CREATE TABLE IF NOT EXISTS exercises (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                body_part TEXT,
                equipment TEXT,
                difficulty TEXT,
                video_path TEXT,
                created_at TEXT
            );

            CREATE TABLE IF NOT EXISTS plans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                plan_date TEXT,
                plan_type TEXT,
                created_at TEXT
            );

            CREATE TABLE IF NOT EXISTS plan_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                plan_id INTEGER,
                exercise_id INTEGER,
                sets INTEGER,
                reps INTEGER,
                weight REAL,
                rest_seconds INTEGER
            );

            CREATE TABLE IF NOT EXISTS progress_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                log_date TEXT,
                weight REAL,
                chest REAL,
                waist REAL,
                arms REAL,
                thighs REAL,
                notes TEXT
            );

            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY,
                theme TEXT
            );

            CREATE TABLE IF NOT EXISTS plan_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                type TEXT,
                created_at TEXT
            );

            CREATE TABLE IF NOT EXISTS template_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                template_id INTEGER,
                exercise_id INTEGER,
                sets INTEGER,
                reps INTEGER,
                rest_seconds INTEGER
            );
            """
        )
        self.connection.commit()
        self.ensure_default_data()

    def ensure_default_data(self) -> None:
        cur = self.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM users WHERE username='admin'")
        if cur.fetchone()[0] == 0:
            cur.execute(
                "INSERT INTO users (full_name, username, password_hash, role, phone, national_id, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    "مدیر سیستم",
                    "admin",
                    hash_password("admin123"),
                    "admin",
                    "09100000000",
                    "0000000000",
                    datetime.utcnow().isoformat(),
                ),
            )
        cur.execute("SELECT COUNT(*) FROM settings WHERE id=?", (CONFIG.settings_id,))
        if cur.fetchone()[0] == 0:
            cur.execute("INSERT INTO settings (id, theme) VALUES (?, ?)", (CONFIG.settings_id, "light"))
        self.connection.commit()

    def cursor(self) -> sqlite3.Cursor:
        return self.connection.cursor()

    def commit(self) -> None:
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()


DB = Database()
