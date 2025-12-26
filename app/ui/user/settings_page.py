from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from app.core.theme_manager import THEME_MANAGER
from app.ui.components.toast import show_toast


class UserSettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("تنظیمات"))
        theme_btn = QPushButton("تغییر تم")
        theme_btn.clicked.connect(self.toggle_theme)
        layout.addWidget(theme_btn)
        layout.addStretch()

    def toggle_theme(self):
        from PySide6.QtWidgets import QApplication

        app = QApplication.instance()
        new_theme = "dark" if THEME_MANAGER.current_theme() == "light" else "light"
        THEME_MANAGER.apply(app, new_theme)  # type: ignore[arg-type]
        show_toast("تم تغییر کرد")
