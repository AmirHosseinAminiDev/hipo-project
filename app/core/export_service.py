"""Export utilities for CSV/PDF outputs."""
from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from .paths import PATHS


class ExportService:
    def __init__(self) -> None:
        self.font_registered = False
        self.font_path = Path(__file__).resolve().parents[1] / "assets" / "fonts" / "Vazirmatn.ttf"

    def register_font(self) -> None:
        if self.font_registered or not self.font_path.exists():
            return
        pdfmetrics.registerFont(TTFont("Vazirmatn", str(self.font_path)))
        self.font_registered = True

    def export_csv(self, headers: list[str], rows: Iterable[Iterable], name: str) -> str:
        target = PATHS.exports / f"{name}.csv"
        with open(target, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for row in rows:
                writer.writerow(row)
        return str(target)

    def export_pdf(self, title: str, headers: list[str], rows: list[list[str]], name: str) -> str:
        self.register_font()
        target = PATHS.exports / f"{name}.pdf"
        c = canvas.Canvas(str(target), pagesize=A4)
        width, height = A4
        c.setTitle(title)
        y = height - 30 * mm
        c.setFont("Vazirmatn" if self.font_registered else "Helvetica", 12)
        c.drawString(20 * mm, y, title)
        y -= 10 * mm
        for header in headers:
            c.drawString(20 * mm, y, header)
            y -= 8 * mm
        y -= 4 * mm
        for row in rows:
            c.drawString(25 * mm, y, " | ".join(map(str, row)))
            y -= 8 * mm
            if y < 20 * mm:
                c.showPage()
                y = height - 20 * mm
        c.save()
        return str(target)


EXPORTER = ExportService()
