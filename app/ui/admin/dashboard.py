from __future__ import annotations

from PySide6.QtWidgets import QWidget, QHBoxLayout, QStackedWidget

from app.ui.components.header import Header
from app.ui.components.sidebar import Sidebar
from app.ui.admin.users_page import UsersPage
from app.ui.admin.exercises_page import ExercisesPage
from app.ui.admin.plans_page import PlansPage
from app.ui.admin.templates_page import TemplatesPage
from app.ui.admin.reports_page import ReportsPage
from app.ui.admin.settings_page import AdminSettingsPage
from app.core.theme_manager import THEME_MANAGER


class AdminDashboard(QWidget):
    def __init__(self, user_row):
        super().__init__()
        self.user_row = user_row
        self.setWindowTitle("داشبورد مدیر")
        self.resize(1200, 720)
        self.stack = QStackedWidget()

        self.users_page = UsersPage()
        self.exercises_page = ExercisesPage()
        self.plans_page = PlansPage()
        self.templates_page = TemplatesPage()
        self.reports_page = ReportsPage()
        self.settings_page = AdminSettingsPage()

        for page in [
            self.users_page,
            self.exercises_page,
            self.plans_page,
            self.templates_page,
            self.reports_page,
            self.settings_page,
        ]:
            self.stack.addWidget(page)

        self.header = Header("داشبورد مدیر", self.close, self.toggle_theme)
        self.sidebar = Sidebar(
            [
                ("کاربران", lambda: self.switch_page(0)),
                ("حرکات", lambda: self.switch_page(1)),
                ("برنامه تمرین", lambda: self.switch_page(2)),
                ("پلن‌های آماده", lambda: self.switch_page(3)),
                ("گزارش‌ها", lambda: self.switch_page(4)),
                ("تنظیمات", lambda: self.switch_page(5)),
            ]
        )

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.sidebar)
        main = QStackedWidget()
        container = QWidget()
        from PySide6.QtWidgets import QVBoxLayout

        v = QVBoxLayout(container)
        v.setContentsMargins(0, 0, 0, 0)
        v.addWidget(self.header)
        v.addWidget(self.stack)
        main.addWidget(container)
        layout.addWidget(main)

    def switch_page(self, index: int):
        self.stack.setCurrentIndex(index)

    def toggle_theme(self):
        from PySide6.QtWidgets import QApplication

        app = QApplication.instance()
        current = THEME_MANAGER.current_theme()
        new_theme = "dark" if current == "light" else "light"
        THEME_MANAGER.apply(app, new_theme)  # type: ignore[arg-type]
