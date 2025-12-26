# BodyBuilderPro

یک اپلیکیشن دسکتاپ حرفه‌ای برای مدیریت باشگاه بدنسازی با PySide6، پایگاه داده SQLite و رابط کاربری فارسی/RTL بر پایه Material Design.

## ویژگی‌ها
- ورود با نقش ادمین و کاربر
- تم روشن/تاریک با ذخیره در دیتابیس
- مدیریت کاربران همراه با اعتبارسنجی موبایل و کدملی و خروجی CSV/PDF
- مدیریت حرکات با ویدیو آفلاین و Drag & Drop
- ساخت برنامه تمرینی، پلن‌های آماده و اعمال تمرین‌ها روی کاربران
- ثبت و گزارش پیشرفت با نمودارهای تعاملی pyqtgraph
- خروجی PDF/CSV فارسی

## نصب و اجرا
1. ایجاد و فعال‌سازی محیط مجازی (اختیاری):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # یا Scripts\\activate در ویندوز
   ```
2. نصب وابستگی‌ها:
   ```bash
   pip install -r requirements.txt
   ```
3. اجرای برنامه:
   ```bash
   python main.py
   ```

> کاربر مدیر پیش‌فرض: `admin` و رمز `admin123`.

## ساخت خروجی exe با PyInstaller
```bash
pyinstaller --noconfirm --noconsole --name BodyBuilderPro --add-data "app/assets;app/assets" main.py
```
- فایل ساخته شده در پوشه `dist/BodyBuilderPro/` قرار می‌گیرد.

## ساخت Installer با Inno Setup
1. پس از ساخت exe، Inno Setup را نصب کنید.
2. فایل `installer/inno_setup_script.iss` را باز کنید و مسیر `Source:` را در صورت نیاز اصلاح کنید.
3. اسکریپت را در Inno Setup اجرا کنید تا `setup.exe` ساخته شود.

## ساختار پروژه
```
BodyBuilderPro/
├─ main.py
├─ app/
│  ├─ core/ (دیتابیس، تنظیمات، مسیرها، تم)
│  ├─ ui/   (صفحات ادمین/کاربر و کامپوننت‌ها)
│  └─ assets/ (استایل‌ها و فونت)
└─ installer/
```

## نکات
- مسیر داده‌ها در ویندوز: `C:\Users\\<username>\\AppData\\Local\\BodyBuilderPro`. پوشه‌های `videos/`, `logs/`, `exports/` به صورت خودکار ساخته می‌شوند.
- برای فونت فارسی می‌توانید فایل `Vazirmatn.ttf` را در مسیر `app/assets/fonts/` قرار دهید.
- اعتبارسنجی کدملی و شماره موبایل در `app/core/validators.py` پیاده‌سازی شده است.
