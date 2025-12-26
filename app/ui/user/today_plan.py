from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem

from app.core.repositories import PLANS
from app.ui.components.video_player import VideoPlayer
from app.core.utils import today


class TodayPlanPage(QWidget):
    def __init__(self, user_row):
        super().__init__()
        self.user_row = user_row
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("تمرینات امروز"))
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.show_video)
        layout.addWidget(self.list_widget)
        self.player = VideoPlayer()
        layout.addWidget(self.player)
        self.refresh()

    def refresh(self):
        self.list_widget.clear()
        for row in PLANS.plan_items_for_date(self.user_row["id"], today()):
            item = QListWidgetItem(
                f"{row['name']} | ست {row['sets']} تکرار {row['reps']} وزن {row['weight']} | استراحت {row['rest_seconds']}s"
            )
            item.setData(256, row)
            self.list_widget.addItem(item)

    def show_video(self, item):
        data = item.data(256)
        self.player.load(data["video_path"])
