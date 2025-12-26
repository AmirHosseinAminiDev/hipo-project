# ✅ SUPER PROFESSIONAL CODEX PROMPT — BodyBuilderPro (PySide6 + SQLite + Offline Videos + Material Design + RTL)

این فایل شامل یک پرامپت حرفه‌ای برای Codex/AI Code Generator است تا یک اپلیکیشن دسکتاپ مدیریت بدنسازی برای ویندوز را **کامل** تولید کند.  
ویژگی‌ها: **Material Design**, **Dark/Light Mode**, **فارسی و RTL**, **ادمین/کاربر**, **ویدیو آفلاین**, **پلن‌های آماده**, **پیشرفت بدن + نمودار**, **Drag & Drop ویدیو**, **Installer با Inno Setup**.

---

## 📌 PROMPT (برای کپی در Codex)

تو یک توسعه‌دهنده‌ی بسیار حرفه‌ای هستی. لطفاً یک اپلیکیشن دسکتاپ حرفه‌ای و کامل برای ویندوز بساز با ویژگی‌های زیر. تمام کدها و فایل‌ها را کامل تولید کن (هیچ بخشی ناقص نباشد). اپلیکیشن باید فارسی، RTL و Material Design واقعی باشد و دارای Light/Dark Mode قابل تغییر باشد.

---

# ✅ نام پروژه:
**BodyBuilderPro**

---

# ✅ تکنولوژی‌ها:
- Python 3.11+
- PySide6 (Qt6)
- SQLite
- QtMultimedia (QMediaPlayer + QVideoWidget)
- Drag & Drop Support
- PyInstaller برای خروجی exe
- Inno Setup برای ساخت Installer (setup.exe)
- نمودارها: **matplotlib یا pyqtgraph** (ترجیح pyqtgraph برای UI مدرن)
- Material Design UI: Qt StyleSheet (QSS) + Components + Typography + Cards + Elevation + Rounded Corners

---

# ✅ نیازمندی‌های UX/UI:
- تمام UI باید RTL باشد
- تمام متن‌ها فارسی
- Material Design واقعی:
  - Card-based UI
  - Buttons با hover/ripple-like effect
  - Rounded corners (12px)
  - Elevation shadows
  - Typography (فونت فارسی Vazirmatn)
- Sidebar در سمت راست
- Header بالا شامل:
  - عنوان صفحه
  - نام کاربر
  - دکمه خروج
  - دکمه تغییر تم (Light/Dark)
- Spacing و Grid استاندارد Material (8px base)
- استفاده از Icons

---

# ✅ قابلیت تغییر تم:
- ThemeManager داشته باشد
- Light Theme و Dark Theme کاملاً Material
- تغییر تم باید بدون ریست برنامه روی کل UI اعمال شود
- تنظیمات تم باید در DB یا JSON در AppData ذخیره شود
- در هر اجرا همان تم قبلی فعال شود

---

# ✅ نقش‌ها:
- Admin
- User

---

# ✅ دیتابیس SQLite (database.db)
در مسیر AppData ذخیره شود.

### users
- id INTEGER PK AUTOINCREMENT
- full_name TEXT
- username TEXT UNIQUE
- password_hash TEXT
- role TEXT (admin/user)
- phone TEXT (شماره موبایل)
- national_id TEXT UNIQUE (کد ملی)
- created_at TEXT

✅ اعتبارسنجی:
- شماره موبایل باید 11 رقم باشد
- کد ملی باید 10 رقم باشد + الگوریتم صحت‌سنجی کد ملی ایران پیاده‌سازی شود (National Code Validation)
- username unique

### exercises
- id INTEGER PK AUTOINCREMENT
- name TEXT
- description TEXT
- body_part TEXT (مثلاً chest, back, legs)
- equipment TEXT (dumbbell/barbell/machine/bodyweight)
- difficulty TEXT (beginner/intermediate/advanced)
- video_path TEXT (offline local path)
- created_at TEXT

### plans
- id INTEGER PK AUTOINCREMENT
- user_id INTEGER (FK users)
- plan_date TEXT (YYYY-MM-DD)
- plan_type TEXT (Push/Pull/Legs/Strength/Custom)
- created_at TEXT

### plan_items
- id INTEGER PK AUTOINCREMENT
- plan_id INTEGER (FK plans)
- exercise_id INTEGER (FK exercises)
- sets INTEGER
- reps INTEGER
- weight REAL NULL (اختیاری)
- rest_seconds INTEGER NULL

### progress_logs
- id INTEGER PK AUTOINCREMENT
- user_id INTEGER (FK users)
- log_date TEXT
- weight REAL (وزن بدن)
- chest REAL NULL
- waist REAL NULL
- arms REAL NULL
- thighs REAL NULL
- notes TEXT NULL

### settings
- id INTEGER PK (always 1)
- theme TEXT (light/dark)

---

# ✅ مسیر AppData در ویندوز:
برنامه باید هنگام اجرا این مسیر را بسازد:
`C:\Users\<username>\AppData\Local\BodyBuilderPro\`

و داخلش:
- database.db
- videos/
- logs/
- exports/

تمام مسیرها در فایل `paths.py` مدیریت شوند.

---

# ✅ 1) صفحه ورود (Login)
- فرم ورود فارسی RTL
- Material Card
- username + password
- پیام‌های فارسی
- ورود موفق → داشبورد نقش مربوطه

---

# ✅ 2) داشبورد Admin
صفحات:
1) مدیریت کاربران
2) مدیریت حرکات + ویدیو
3) برنامه‌ریزی تمرین
4) پلن‌های آماده (Push/Pull/Strength)
5) گزارش‌ها و آمار
6) تنظیمات

---

# ✅ 3) مدیریت کاربران (Admin)
- لیست کاربران (Material Table)
- افزودن/ویرایش/حذف
- ذخیره:
  - نام کامل
  - username
  - password
  - phone
  - national_id
  - role
- جستجوی حرفه‌ای:
  - سرچ با نام، موبایل، کد ملی، یوزرنیم
- امکان خروجی گرفتن از لیست کاربران به CSV

---

# ✅ 4) مدیریت حرکات و ویدیوها (Admin)
## افزودن حرکت:
- name
- description
- body_part
- equipment
- difficulty
- آپلود ویدیو (offline)

✅ Drag & Drop:
- امکان drag video file داخل پنل اضافه کردن حرکت
- با drop شدن فایل:
  - کپچر مسیر فایل
  - نمایش preview اسم فایل
  - امکان آپلود و ذخیره

✅ هنگام ذخیره:
- فایل ویدیو به videos/ کپی شود
- نام فایل UUID شود
- video_path در DB ذخیره شود

✅ امکانات:
- لیست حرکات به شکل Card Grid + امکان List View
- جستجوی حرفه‌ای:
  - سرچ متنی (نام/توضیحات)
  - فیلتر body_part
  - فیلتر difficulty
  - فیلتر equipment
  - مرتب‌سازی (جدیدترین/قدیمی‌ترین/نام)
- preview ویدیو در برنامه
- حذف حرکت = حذف از DB و حذف فایل ویدیو

---

# ✅ 5) برنامه‌ریزی تمرین (Admin)
Admin بتواند برای هر کاربر برنامه روزانه بسازد.
- انتخاب user
- انتخاب تاریخ
- انتخاب نوع پلن:
  - Push
  - Pull
  - Legs
  - Strength
  - Custom
- افزودن تمرین:
  - انتخاب exercise
  - sets/reps
  - weight (اختیاری)
  - rest time
- ذخیره برنامه

---

# ✅ 6) پلن‌های آماده (Admin)
Admin بتواند template بسازد:
- Push/Pull/Legs Template
- Strength Template
- Custom Template

Template ها قابل استفاده برای تولید سریع برنامه کاربران باشند.

جدول‌های جدید:
### plan_templates
- id
- name
- type (PPL/Strength/Custom)
- created_at

### template_items
- id
- template_id
- exercise_id
- sets
- reps
- rest_seconds

Admin بتواند template را روی کاربر اعمال کند.

---

# ✅ 7) داشبورد User
صفحات:
1) برنامه امروز
2) برنامه هفته
3) تمرینات و ویدیوها (فقط مشاهده)
4) ثبت پیشرفت
5) نمودار پیشرفت
6) تنظیمات (تم)

---

# ✅ 8) برنامه امروز (User)
- نمایش تمرینات امروز به شکل Card
- هر Card:
  - نام حرکت
  - sets/reps/rest/weight
  - دکمه "مشاهده ویدیو آموزشی"
- پخش ویدیو داخل اپ:
  - QMediaPlayer + QVideoWidget
  - کنترل کامل پخش
  - Fullscreen

---

# ✅ 9) برنامه هفته (User)
- لیست روزهای هفته با تمرینات
- انتخاب روز → نمایش برنامه آن روز

---

# ✅ 10) پیگیری پیشرفت (User)
User بتواند داده‌های بدن را ثبت کند:
- تاریخ
- وزن بدن
- دور سینه
- دور کمر
- دور بازو
- دور ران
- یادداشت

و در نمودارها نمایش داده شود:
- نمودار وزن در طول زمان
- نمودار دور کمر
- نمودارها interactive (pyqtgraph ترجیحاً)

Admin هم بتواند progress کاربران را مشاهده کند.

---

# ✅ 11) سیستم Export
- خروجی PDF یا CSV از:
  - برنامه تمرینی
  - گزارش پیشرفت
- PDF با فونت فارسی و راست‌چین

---

# ✅ امنیت:
- password_hash با bcrypt
- role-based access
- جلوگیری از SQL injection
- نمایش خطاها با پیام فارسی

---

# ✅ ساختار پروژه (Professional):
```
BodyBuilderPro/
│─ main.py
│─ requirements.txt
│─ README.md
│
├─ app/
│   ├─ core/
│   │   ├─ config.py
│   │   ├─ paths.py
│   │   ├─ database.py
│   │   ├─ models.py
│   │   ├─ repositories.py
│   │   ├─ security.py
│   │   ├─ theme_manager.py
│   │   ├─ validators.py
│   │   ├─ export_service.py
│   │   └─ utils.py
│   │
│   ├─ ui/
│   │   ├─ login.py
│   │   ├─ admin/
│   │   │   ├─ dashboard.py
│   │   │   ├─ users_page.py
│   │   │   ├─ exercises_page.py
│   │   │   ├─ plans_page.py
│   │   │   ├─ templates_page.py
│   │   │   ├─ reports_page.py
│   │   │   └─ settings_page.py
│   │
│   │   ├─ user/
│   │   │   ├─ dashboard.py
│   │   │   ├─ today_plan.py
│   │   │   ├─ week_plan.py
│   │   │   ├─ progress_page.py
│   │   │   ├─ progress_charts.py
│   │   │   └─ settings_page.py
│   │
│   │   ├─ components/
│   │   │   ├─ sidebar.py
│   │   │   ├─ header.py
│   │   │   ├─ material_card.py
│   │   │   ├─ material_button.py
│   │   │   ├─ material_input.py
│   │   │   ├─ material_table.py
│   │   │   ├─ toast.py
│   │   │   ├─ dialogs.py
│   │   │   ├─ filters_panel.py
│   │   │   └─ video_player.py
│   │
│   └─ assets/
│       ├─ fonts/
│       │   └─ Vazirmatn.ttf
│       ├─ icons/
│       └─ styles/
│           ├─ material_light.qss
│           └─ material_dark.qss
│
└─ installer/
    ├─ inno_setup_script.iss
    └─ build_installer.md
```

---

# ✅ بخش Installer با Inno Setup:
- یک فایل `installer/inno_setup_script.iss` تولید کن که:
  - فایل exe ساخته شده را نصب کند
  - shortcut روی Desktop بسازد
  - shortcut در Start Menu بسازد
  - مسیر نصب به Program Files
  - داده‌ها در AppData ذخیره می‌شوند و پاک نشوند
- در README توضیح بده چطور با Inno Setup خروجی setup.exe بگیریم

---

# ✅ خروجی‌ها:
1) requirements.txt
2) README.md فارسی شامل:
   - نصب و اجرا
   - ساخت exe
   - ساخت Installer
3) فایل Inno Setup script (.iss) برای ساخت setup.exe
4) ایجاد admin پیشفرض:
   - username: admin
   - password: admin123
5) تمام UI فارسی و RTL و Material Design

---

# ✅ درخواست نهایی:
کد را کامل تولید کن، هیچ بخشی را ناقص نگذار. همه فایل‌ها را با مسیر کامل بنویس. UI کاملاً RTL، Material و حرفه‌ای باشد. پروژه باید قابل اجرا باشد.

---

## ✅ END PROMPT

---

### ✅ نکته برای بهبود خروجی Codex
اگر می‌خواهی کیفیت خروجی بهتر شود این خط را نیز به انتهای پرامپت اضافه کن:

> کد را ماژولار، تمیز، با کلاس‌های قابل تست و بدون تکرار بنویس. از الگوی Repository + Service استفاده کن.
