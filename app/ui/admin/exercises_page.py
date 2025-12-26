from __future__ import annotations

import os
from datetime import datetime

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QPushButton,
    QFileDialog,
    QListWidget,
)
from PySide6.QtCore import Qt

from app.core.models import Exercise
from app.core.paths import PATHS
from app.core.repositories import EXERCISES
from app.ui.components.toast import show_toast
from app.ui.components.video_player import VideoPlayer


class ExercisesPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)

        left = QVBoxLayout()
        left.addWidget(QLabel("افزودن حرکت"))
        self.name = QLineEdit(); self.name.setPlaceholderText("نام حرکت")
        self.desc = QTextEdit(); self.desc.setPlaceholderText("توضیح")
        self.body = QComboBox(); self.body.addItems(["chest", "back", "legs", "arms", "shoulders"])
        self.equipment = QComboBox(); self.equipment.addItems(["dumbbell", "barbell", "machine", "bodyweight"])
        self.difficulty = QComboBox(); self.difficulty.addItems(["beginner", "intermediate", "advanced"])
        self.video_path = QLineEdit(); self.video_path.setPlaceholderText("مسیر ویدیو")
        browse = QPushButton("انتخاب فایل")
        browse.clicked.connect(self.pick_file)
        save_btn = QPushButton("ذخیره")
        save_btn.clicked.connect(self.save)
        self.video_player = VideoPlayer()

        for w in [self.name, self.desc, self.body, self.equipment, self.difficulty, self.video_path, browse, save_btn, self.video_player]:
            left.addWidget(w)
        left.addStretch()

        right = QVBoxLayout()
        right.addWidget(QLabel("حرکات"))
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.preview_video)
        delete_btn = QPushButton("حذف")
        delete_btn.clicked.connect(self.delete_selected)
        right.addWidget(self.list_widget)
        right.addWidget(delete_btn)

        layout.addLayout(left, 2)
        layout.addLayout(right, 3)
        self.setAcceptDrops(True)
        self.refresh()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            self.video_path.setText(urls[0].toLocalFile())
            show_toast("فایل ویدیو انتخاب شد")

    def pick_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "انتخاب ویدیو", "", "ویدیو (*.mp4 *.mov *.mkv)")
        if path:
            self.video_path.setText(path)

    def save(self):
        try:
            stored_path = PATHS.copy_video(self.video_path.text())
        except Exception as exc:
            show_toast(str(exc))
            return
        ex = Exercise(
            name=self.name.text(),
            description=self.desc.toPlainText(),
            body_part=self.body.currentText(),
            equipment=self.equipment.currentText(),
            difficulty=self.difficulty.currentText(),
            video_path=stored_path,
            created_at=datetime.utcnow().isoformat(),
        )
        EXERCISES.create(ex)
        show_toast("حرکت ذخیره شد")
        self.refresh()

    def refresh(self):
        self.list_widget.clear()
        for row in EXERCISES.all():
            self.list_widget.addItem(f"{row['name']} | {row['body_part']} | {row['difficulty']}")
            self.list_widget.item(self.list_widget.count()-1).setData(Qt.UserRole, row)

    def preview_video(self, item):
        data = item.data(Qt.UserRole)
        path = data["video_path"]
        if os.path.exists(path):
            self.video_player.load(path)

    def delete_selected(self):
        item = self.list_widget.currentItem()
        if not item:
            return
        row = item.data(Qt.UserRole)
        EXERCISES.delete(row["id"])
        try:
            os.remove(row["video_path"])
        except OSError:
            pass
        show_toast("حذف شد")
        self.refresh()
