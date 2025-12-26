from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from app.core.theme_manager import THEME_MANAGER
from app.ui.login import LoginWindow


def main():
    app = QApplication(sys.argv)
    # Apply persisted theme
    THEME_MANAGER.apply(app, THEME_MANAGER.current_theme())
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
