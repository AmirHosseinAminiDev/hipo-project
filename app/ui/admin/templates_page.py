from __future__ import annotations

from datetime import datetime

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QListWidget, QHBoxLayout

from app.core.repositories import EXERCISES, DB
from app.ui.components.toast import show_toast


class TemplatesPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("پلن‌های آماده"))
        form = QHBoxLayout()
        self.name = QLineEdit(); self.name.setPlaceholderText("نام قالب")
        self.type = QComboBox(); self.type.addItems(["PPL", "Strength", "Custom"])
        self.exercise = QComboBox()
        for e in EXERCISES.all():
            self.exercise.addItem(e["name"], e["id"])
        self.sets = QLineEdit(); self.sets.setPlaceholderText("ست")
        self.reps = QLineEdit(); self.reps.setPlaceholderText("تکرار")
        add_btn = QPushButton("ایجاد قالب")
        add_btn.clicked.connect(self.create_template)
        for w in [self.name, self.type, self.exercise, self.sets, self.reps, add_btn]:
            form.addWidget(w)
        layout.addLayout(form)
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        self.refresh()

    def refresh(self):
        cur = DB.cursor()
        cur.execute("SELECT * FROM plan_templates ORDER BY created_at DESC")
        self.list_widget.clear()
        for row in cur.fetchall():
            self.list_widget.addItem(f"{row['name']} | {row['type']}")

    def create_template(self):
        cur = DB.cursor()
        cur.execute(
            "INSERT INTO plan_templates (name, type, created_at) VALUES (?, ?, ?)",
            (self.name.text(), self.type.currentText(), datetime.utcnow().isoformat()),
        )
        template_id = cur.lastrowid
        cur.execute(
            "INSERT INTO template_items (template_id, exercise_id, sets, reps, rest_seconds) VALUES (?, ?, ?, ?, ?)",
            (template_id, self.exercise.currentData(), int(self.sets.text() or 0), int(self.reps.text() or 0), 60),
        )
        DB.commit()
        show_toast("قالب ساخته شد")
        self.refresh()
