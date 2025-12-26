# ساخت نصاب BodyBuilderPro با Inno Setup

1. ابتدا با PyInstaller خروجی exe بسازید:
   ```bash
   pyinstaller --noconfirm --noconsole --name BodyBuilderPro --add-data "app/assets;app/assets" main.py
   ```
2. Inno Setup را نصب کنید و فایل `installer/inno_setup_script.iss` را باز کنید.
3. در صورت تغییر مسیر خروجی PyInstaller، بخش `Source` را در اسکریپت به مسیر جدید exe و پوشه `app` اصلاح کنید.
4. روی دکمه Build در Inno Setup کلیک کنید تا فایل `BodyBuilderPro_Setup.exe` ساخته شود.
5. نصب‌کننده میانبرهای دسکتاپ و Start Menu را ایجاد می‌کند و داده‌ها در AppData باقی می‌مانند.
