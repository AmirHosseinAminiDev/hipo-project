from __future__ import annotations

from datetime import datetime

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QFileDialog,
)

from app.core.models import User
from app.core.repositories import USERS
from app.core.security import hash_password
from app.core.validators import is_valid_phone, is_valid_national_id
from app.ui.components.material_table import MaterialTable
from app.ui.components.toast import show_toast
from app.core.export_service import EXPORTER


class UsersPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("مدیریت کاربران"))
        self.table = MaterialTable()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["نام", "نام کاربری", "نقش", "موبایل", "کد ملی", "ایجاد شده"]
        )

        form = QHBoxLayout()
        self.full_name = QLineEdit(); self.full_name.setPlaceholderText("نام کامل")
        self.username = QLineEdit(); self.username.setPlaceholderText("نام کاربری")
        self.password = QLineEdit(); self.password.setPlaceholderText("رمز عبور")
        self.password.setEchoMode(QLineEdit.Password)
        self.phone = QLineEdit(); self.phone.setPlaceholderText("شماره موبایل")
        self.national_id = QLineEdit(); self.national_id.setPlaceholderText("کد ملی")
        self.role = QComboBox(); self.role.addItems(["admin", "user"])
        add_btn = QPushButton("افزودن")
        add_btn.clicked.connect(self.add_user)
        export_btn = QPushButton("خروجی CSV")
        export_btn.clicked.connect(self.export_csv)

        for w in [self.full_name, self.username, self.password, self.phone, self.national_id, self.role, add_btn, export_btn]:
            form.addWidget(w)

        layout.addLayout(form)
        layout.addWidget(self.table)
        self.refresh()

    def refresh(self):
        rows = list(USERS.all())
        self.table.setRowCount(len(rows))
        for idx, row in enumerate(rows):
            for col, key in enumerate(["full_name", "username", "role", "phone", "national_id", "created_at"]):
                from PySide6.QtWidgets import QTableWidgetItem

                self.table.setItem(idx, col, QTableWidgetItem(str(row[key])))

    def add_user(self):
        phone = self.phone.text().strip()
        national_id = self.national_id.text().strip()
        if not is_valid_phone(phone):
            show_toast("شماره موبایل نامعتبر است")
            return
        if not is_valid_national_id(national_id):
            show_toast("کد ملی نامعتبر است")
            return
        user = User(
            full_name=self.full_name.text(),
            username=self.username.text(),
            password_hash=hash_password(self.password.text()),
            role=self.role.currentText(),
            phone=phone,
            national_id=national_id,
            created_at=datetime.utcnow().isoformat(),
        )
        try:
            USERS.create(user)
        except Exception as exc:  # pragma: no cover - sqlite errors
            show_toast(f"خطا: {exc}")
            return
        show_toast("کاربر اضافه شد")
        self.refresh()

    def export_csv(self):
        rows = USERS.all()
        headers = ["نام", "نام کاربری", "نقش", "موبایل", "کد ملی"]
        path = EXPORTER.export_csv(headers, [[r["full_name"], r["username"], r["role"], r["phone"], r["national_id"]] for r in rows], "users")
        QFileDialog.getSaveFileName(self, "مسیر ذخیره", path)
        show_toast("خروجی CSV آماده شد")
