"""Application configuration constants and helpers."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    app_name: str = "BodyBuilderPro"
    db_name: str = "database.db"
    settings_id: int = 1

    @property
    def appdata_base(self) -> str:
        return os.getenv(
            "BODYBUILDERPRO_APPDATA",
            os.path.join(os.path.expanduser("~"), "AppData", "Local", self.app_name),
        )


CONFIG = AppConfig()
