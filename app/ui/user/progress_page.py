from __future__ import annotations

from datetime import datetime

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QHBoxLayout,
)

from app.core.models import ProgressLog
from app.core.repositories import PROGRESS
from app.ui.components.toast import show_toast


class ProgressPage(QWidget):
    def __init__(self, user_row):
        super().__init__()
        self.user_row = user_row
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("ثبت پیشرفت"))
        form = QHBoxLayout()
        self.weight = QLineEdit(); self.weight.setPlaceholderText("وزن")
        self.chest = QLineEdit(); self.chest.setPlaceholderText("سینه")
        self.waist = QLineEdit(); self.waist.setPlaceholderText("کمر")
        self.arms = QLineEdit(); self.arms.setPlaceholderText("بازو")
        self.thighs = QLineEdit(); self.thighs.setPlaceholderText("ران")
        self.notes = QTextEdit(); self.notes.setPlaceholderText("یادداشت")
        save = QPushButton("ثبت")
        save.clicked.connect(self.save)
        for w in [self.weight, self.chest, self.waist, self.arms, self.thighs, save]:
            form.addWidget(w)
        layout.addLayout(form)
        layout.addWidget(self.notes)
        layout.addStretch()

    def save(self):
        entry = ProgressLog(
            user_id=self.user_row["id"],
            log_date=datetime.utcnow().date().isoformat(),
            weight=float(self.weight.text() or 0),
            chest=float(self.chest.text() or 0),
            waist=float(self.waist.text() or 0),
            arms=float(self.arms.text() or 0),
            thighs=float(self.thighs.text() or 0),
            notes=self.notes.toPlainText(),
        )
        PROGRESS.log(entry)
        show_toast("ثبت شد")
