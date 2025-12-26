from __future__ import annotations

from PySide6.QtWidgets import QTableWidget


class MaterialTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MaterialTable")
        self.setAlternatingRowColors(True)
        self.setStyleSheet(
            """
            QTableWidget#MaterialTable {
                gridline-color: rgba(0,0,0,0.05);
                selection-background-color: #4caf50;
                border: none;
            }
            """
        )
