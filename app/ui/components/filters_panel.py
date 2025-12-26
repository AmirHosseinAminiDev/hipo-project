from __future__ import annotations

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QLineEdit


class FiltersPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.search = QLineEdit()
        self.search.setPlaceholderText("جستجو")
        self.body_filter = QComboBox()
        self.body_filter.addItems(["همه", "chest", "back", "legs", "arms", "shoulders"])
        self.diff_filter = QComboBox()
        self.diff_filter.addItems(["همه", "beginner", "intermediate", "advanced"])
        layout.addWidget(QLabel("جستجو:"))
        layout.addWidget(self.search)
        layout.addWidget(QLabel("عضله:"))
        layout.addWidget(self.body_filter)
        layout.addWidget(QLabel("سطح:"))
        layout.addWidget(self.diff_filter)
        layout.addStretch()
