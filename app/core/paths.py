"""Path utilities for BodyBuilderPro."""
from __future__ import annotations

import os
import shutil
import uuid
from pathlib import Path

from .config import CONFIG


class Paths:
    def __init__(self) -> None:
        base = Path(CONFIG.appdata_base)
        self.base = base
        self.videos = base / "videos"
        self.logs = base / "logs"
        self.exports = base / "exports"
        self.db_path = base / CONFIG.db_name
        self.ensure()

    def ensure(self) -> None:
        for folder in [self.base, self.videos, self.logs, self.exports]:
            folder.mkdir(parents=True, exist_ok=True)

    def copy_video(self, source_path: str) -> str:
        """Copy a video file to the managed videos directory with a UUID name."""
        src = Path(source_path)
        if not src.exists():
            raise FileNotFoundError(f"ویدیو یافت نشد: {source_path}")
        extension = src.suffix or ".mp4"
        target = self.videos / f"{uuid.uuid4()}{extension}"
        shutil.copy2(src, target)
        return str(target)


PATHS = Paths()
