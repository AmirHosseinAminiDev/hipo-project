from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):
    def __init__(self, items: list[tuple[str, callable]], parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)
        for label, handler in items:
            btn = QPushButton(label)
            btn.setObjectName("SidebarButton")
            btn.clicked.connect(handler)
            layout.addWidget(btn)
        layout.addStretch()
