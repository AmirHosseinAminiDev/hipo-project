from __future__ import annotations

from PySide6.QtWidgets import QFrame
from PySide6.QtGui import QColor, QPainter, QBrush
from PySide6.QtCore import Qt


class MaterialCard(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MaterialCard")
        self.setStyleSheet(
            """
            QFrame#MaterialCard {
                background: palette(base);
                border-radius: 12px;
                padding: 12px;
                border: 1px solid rgba(255,255,255,0.04);
            }
            """
        )
        self.setAutoFillBackground(False)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(0, 0, 0, 20)))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 12, 12)
