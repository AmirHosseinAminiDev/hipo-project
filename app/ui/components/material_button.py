from __future__ import annotations

from PySide6.QtWidgets import QPushButton


class MaterialButton(QPushButton):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setObjectName("MaterialButton")
        self.setCursor("pointinghand")
        self.setStyleSheet(
            """
            QPushButton#MaterialButton {
                border-radius: 10px;
                padding: 10px 16px;
                background: #4caf50;
                color: white;
                font-weight: 600;
            }
            QPushButton#MaterialButton:hover {
                background: #43a047;
            }
            QPushButton#MaterialButton:pressed {
                background: #388e3c;
            }
            """
        )
