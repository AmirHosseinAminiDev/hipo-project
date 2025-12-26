from __future__ import annotations

from PySide6.QtWidgets import QLineEdit


class MaterialLineEdit(QLineEdit):
    def __init__(self, placeholder: str = "", parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setObjectName("MaterialLineEdit")
        self.setStyleSheet(
            """
            QLineEdit#MaterialLineEdit {
                padding: 10px 12px;
                border-radius: 10px;
                border: 1px solid #777;
            }
            QLineEdit#MaterialLineEdit:focus {
                border-color: #4caf50;
            }
            """
        )
