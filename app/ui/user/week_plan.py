from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget

from app.core.repositories import PLANS


class WeekPlanPage(QWidget):
    def __init__(self, user_row):
        super().__init__()
        self.user_row = user_row
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("برنامه هفته"))
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        self.refresh()

    def refresh(self):
        self.list_widget.clear()
        for row in PLANS.plans_for_user(self.user_row["id"]):
            self.list_widget.addItem(f"{row['plan_date']} | {row['plan_type']} | {row['exercise_names']}")
