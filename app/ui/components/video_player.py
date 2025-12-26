from __future__ import annotations

from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget


class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.video_widget = QVideoWidget()
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)
        self.play_button = QPushButton("پخش/توقف")
        self.play_button.clicked.connect(self.toggle)
        layout.addWidget(self.video_widget)
        layout.addWidget(self.play_button)

    def load(self, path: str) -> None:
        self.player.setSource(QUrl.fromLocalFile(path))

    def toggle(self) -> None:
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()
