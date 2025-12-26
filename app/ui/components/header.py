from __future__ import annotations

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


class Header(QWidget):
    def __init__(self, title: str, on_logout, on_toggle_theme, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("font-size:18px;font-weight:700;")
        self.theme_btn = QPushButton("تغییر تم")
        self.logout_btn = QPushButton("خروج")
        self.theme_btn.clicked.connect(on_toggle_theme)
        self.logout_btn.clicked.connect(on_logout)
        layout.addWidget(self.title_label)
        layout.addStretch()
        layout.addWidget(self.theme_btn)
        layout.addWidget(self.logout_btn)

    def set_title(self, title: str) -> None:
        self.title_label.setText(title)
