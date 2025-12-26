from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from app.core.repositories import USERS, PLANS, PROGRESS
from app.core.export_service import EXPORTER
from app.ui.components.toast import show_toast


class ReportsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("گزارش‌ها و خروجی"))
        export_users = QPushButton("خروجی کاربران PDF")
        export_users.clicked.connect(self.export_users_pdf)
        export_progress = QPushButton("خروجی پیشرفت CSV")
        export_progress.clicked.connect(self.export_progress_csv)
        layout.addWidget(export_users)
        layout.addWidget(export_progress)
        layout.addStretch()

    def export_users_pdf(self):
        rows = USERS.all()
        headers = ["نام", "نام کاربری", "نقش"]
        data = [[r["full_name"], r["username"], r["role"]] for r in rows]
        EXPORTER.export_pdf("گزارش کاربران", headers, data, "users_report")
        show_toast("PDF آماده شد")

    def export_progress_csv(self):
        rows = []
        for user in USERS.all():
            for log in PROGRESS.logs_for_user(user["id"]):
                rows.append([
                    user["full_name"], log["log_date"], log["weight"], log["waist"], log["chest"], log["arms"], log["thighs"], log["notes"],
                ])
        headers = ["کاربر", "تاریخ", "وزن", "کمر", "سینه", "بازو", "ران", "یادداشت"]
        EXPORTER.export_csv(headers, rows, "progress_report")
        show_toast("CSV آماده شد")
