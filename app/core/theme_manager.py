"""Theme manager to switch between light and dark Material themes."""
from __future__ import annotations

from pathlib import Path
from typing import Literal

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QApplication

from .paths import PATHS
from .repositories import SETTINGS

ThemeName = Literal["light", "dark"]


class ThemeManager:
    def __init__(self) -> None:
        self.assets_dir = Path(__file__).resolve().parents[1] / "assets"
        self.styles_dir = self.assets_dir / "styles"
        self.font_path = self.assets_dir / "fonts" / "Vazirmatn.ttf"
        self.ensure_font()

    def ensure_font(self) -> None:
        if self.font_path.exists():
            QFontDatabase.addApplicationFont(str(self.font_path))

    def load_qss(self, theme: ThemeName) -> str:
        qss_file = self.styles_dir / f"material_{theme}.qss"
        if qss_file.exists():
            return qss_file.read_text(encoding="utf-8")
        return ""

    def apply(self, app: QApplication, theme: ThemeName) -> None:
        qss = self.load_qss(theme)
        app.setStyleSheet(qss)
        SETTINGS.set_theme(theme)

    def current_theme(self) -> ThemeName:
        return SETTINGS.get_theme()  # type: ignore[return-value]


THEME_MANAGER = ThemeManager()
