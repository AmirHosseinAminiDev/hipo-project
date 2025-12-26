from __future__ import annotations

from PySide6.QtWidgets import QLabel, QApplication
from PySide6.QtCore import Qt, QTimer


def show_toast(message: str, timeout: int = 2500) -> None:
    label = QLabel(message)
    label.setWindowFlags(Qt.ToolTip)
    label.setStyleSheet(
        """
        QLabel {
            background: rgba(0,0,0,0.8);
            color: white;
            padding: 10px 16px;
            border-radius: 8px;
            font-weight: 600;
        }
        """
    )
    label.adjustSize()
    cursor = QApplication.primaryScreen().availableGeometry().center()
    label.move(cursor.x() - label.width() // 2, cursor.y())
    label.show()
    QTimer.singleShot(timeout, label.close)
