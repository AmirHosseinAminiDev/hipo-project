from __future__ import annotations

from PySide6.QtWidgets import QWidget, QHBoxLayout, QStackedWidget, QVBoxLayout

from app.ui.components.header import Header
from app.ui.components.sidebar import Sidebar
from app.ui.user.today_plan import TodayPlanPage
from app.ui.user.week_plan import WeekPlanPage
from app.ui.user.progress_page import ProgressPage
from app.ui.user.settings_page import UserSettingsPage
from app.ui.user.progress_charts import ProgressCharts
from app.core.theme_manager import THEME_MANAGER


class UserDashboard(QWidget):
    def __init__(self, user_row):
        super().__init__()
        self.user_row = user_row
        self.setWindowTitle("داشبورد کاربر")
        self.resize(1100, 700)
        self.stack = QStackedWidget()
        self.today_page = TodayPlanPage(user_row)
        self.week_page = WeekPlanPage(user_row)
        self.progress_page = ProgressPage(user_row)
        self.charts_page = ProgressCharts(user_row)
        self.settings_page = UserSettingsPage()
        for page in [self.today_page, self.week_page, self.progress_page, self.charts_page, self.settings_page]:
            self.stack.addWidget(page)

        self.header = Header("برنامه امروز", self.close, self.toggle_theme)
        self.sidebar = Sidebar(
            [
                ("برنامه امروز", lambda: self.switch_page(0)),
                ("برنامه هفته", lambda: self.switch_page(1)),
                ("ثبت پیشرفت", lambda: self.switch_page(2)),
                ("نمودارها", lambda: self.switch_page(3)),
                ("تنظیمات", lambda: self.switch_page(4)),
            ]
        )
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.sidebar)
        container = QWidget()
        v = QVBoxLayout(container)
        v.setContentsMargins(0, 0, 0, 0)
        v.addWidget(self.header)
        v.addWidget(self.stack)
        layout.addWidget(container)

    def switch_page(self, index: int):
        self.stack.setCurrentIndex(index)

    def toggle_theme(self):
        from PySide6.QtWidgets import QApplication

        app = QApplication.instance()
        new_theme = "dark" if THEME_MANAGER.current_theme() == "light" else "light"
        THEME_MANAGER.apply(app, new_theme)  # type: ignore[arg-type]
