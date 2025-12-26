from __future__ import annotations

import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from app.core.repositories import PROGRESS


class ProgressCharts(QWidget):
    def __init__(self, user_row):
        super().__init__()
        self.user_row = user_row
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("نمودار پیشرفت"))
        self.weight_plot = pg.PlotWidget(title="وزن")
        self.waist_plot = pg.PlotWidget(title="دور کمر")
        layout.addWidget(self.weight_plot)
        layout.addWidget(self.waist_plot)
        self.refresh()

    def refresh(self):
        logs = list(reversed(PROGRESS.logs_for_user(self.user_row["id"])))
        xs = list(range(len(logs)))
        weights = [log["weight"] for log in logs]
        waist = [log["waist"] for log in logs]
        self.weight_plot.clear(); self.weight_plot.plot(xs, weights, pen=pg.mkPen("#4caf50", width=2), symbol="o")
        self.waist_plot.clear(); self.waist_plot.plot(xs, waist, pen=pg.mkPen("#2196f3", width=2), symbol="o")
