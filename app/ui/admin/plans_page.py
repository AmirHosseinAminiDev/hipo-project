from __future__ import annotations

from datetime import datetime

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QDateEdit,
    QPushButton,
    QSpinBox,
    QListWidget,
)
from PySide6.QtCore import QDate, Qt

from app.core.models import Plan, PlanItem
from app.core.repositories import USERS, EXERCISES, PLANS
from app.ui.components.toast import show_toast


class PlansPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("برنامه‌ریزی تمرین"))
        form = QHBoxLayout()
        self.user_combo = QComboBox()
        for u in USERS.all():
            self.user_combo.addItem(u["full_name"], u["id"])
        self.date_edit = QDateEdit(QDate.currentDate())
        self.plan_type = QComboBox(); self.plan_type.addItems(["Push", "Pull", "Legs", "Strength", "Custom"])
        self.exercise_combo = QComboBox()
        for e in EXERCISES.all():
            self.exercise_combo.addItem(e["name"], e["id"])
        self.sets = QSpinBox(); self.sets.setValue(3)
        self.reps = QSpinBox(); self.reps.setValue(12)
        self.weight = QSpinBox(); self.weight.setMaximum(500)
        self.rest = QSpinBox(); self.rest.setMaximum(600)
        add_btn = QPushButton("افزودن تمرین")
        add_btn.clicked.connect(self.add_item)
        save_btn = QPushButton("ذخیره برنامه")
        save_btn.clicked.connect(self.save_plan)
        for w in [self.user_combo, self.date_edit, self.plan_type, self.exercise_combo, self.sets, self.reps, self.weight, self.rest, add_btn, save_btn]:
            form.addWidget(w)
        layout.addLayout(form)
        self.items_list = QListWidget()
        layout.addWidget(self.items_list)
        self.items: list[PlanItem] = []

    def add_item(self):
        exercise_id = self.exercise_combo.currentData()
        item = PlanItem(
            plan_id=-1,
            exercise_id=exercise_id,
            sets=self.sets.value(),
            reps=self.reps.value(),
            weight=float(self.weight.value()),
            rest_seconds=self.rest.value(),
        )
        self.items.append(item)
        self.items_list.addItem(
            f"{self.exercise_combo.currentText()} | {item.sets}x{item.reps} | {item.weight}kg | استراحت {item.rest_seconds}s"
        )

    def save_plan(self):
        if not self.items:
            show_toast("تمرینی اضافه نشده")
            return
        user_id = self.user_combo.currentData()
        plan = Plan(
            user_id=user_id,
            plan_date=self.date_edit.date().toString("yyyy-MM-dd"),
            plan_type=self.plan_type.currentText(),
            created_at=datetime.utcnow().isoformat(),
        )
        plan_id = PLANS.create(plan)
        for item in self.items:
            item.plan_id = plan_id
        PLANS.add_items(self.items)
        show_toast("برنامه ذخیره شد")
        self.items.clear()
        self.items_list.clear()
