from __future__ import annotations

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from app.core.security import verify_password
from app.core.repositories import USERS
from app.ui.admin.dashboard import AdminDashboard
from app.ui.user.dashboard import UserDashboard
from app.ui.components.material_card import MaterialCard
from app.ui.components.toast import show_toast


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ورود به BodyBuilderPro")
        self.setFixedSize(420, 320)
        main_layout = QVBoxLayout(self)
        card = MaterialCard()
        form = QVBoxLayout(card)
        title = QLabel("ورود")
        title.setStyleSheet("font-size:22px;font-weight:700;")
        self.username = QLineEdit()
        self.username.setPlaceholderText("نام کاربری")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("رمز عبور")
        login_btn = QPushButton("ورود")
        login_btn.clicked.connect(self.handle_login)
        form.addWidget(title)
        form.addSpacing(12)
        form.addWidget(self.username)
        form.addWidget(self.password)
        form.addSpacing(12)
        form.addWidget(login_btn)
        main_layout.addStretch()
        main_layout.addWidget(card)
        main_layout.addStretch()

    def handle_login(self):
        username = self.username.text().strip()
        password = self.password.text()
        user = USERS.get_by_username(username)
        if not user or not verify_password(password, user["password_hash"]):
            show_toast("نام کاربری یا رمز عبور اشتباه است")
            return
        self.accept()
        role = user["role"]
        if role == "admin":
            self.dashboard = AdminDashboard(user)
        else:
            self.dashboard = UserDashboard(user)
        self.dashboard.show()


def run_login(app: QApplication):
    login = LoginWindow()
    login.show()
    return app.exec()
