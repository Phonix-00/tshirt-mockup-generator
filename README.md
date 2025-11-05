# T-Shirt Mockup Generator API

یک API برای تولید خودکار موکاپ تیشرت با متن دلخواه کاربر.

## 🎯 ویژگی‌ها

- ✅ تولید موکاپ تیشرت با متن سفارشی
- ✅ پشتیبانی از 4 رنگ تیشرت (سیاه، سفید، آبی، زرد)
- ✅ پردازش ناهمزمان با Celery
- ✅ RESTful API
- ✅ ذخیره‌سازی در Database

## 🛠️ تکنولوژی‌های استفاده شده

- **Django 4.2** - فریمورک اصلی
- **Django REST Framework** - ساخت API
- **Celery 5.5** - پردازش پس‌زمینه
- **Redis 7.0** - Message Broker
- **Pillow 12.0** - پردازش تصویر
- **SQLite** - دیتابیس

## 📋 پیش‌نیازها

- Python 3.10+
- Redis Server
- Git

## 🚀 نصب و راه‌اندازی

### 1. کلون کردن پروژه
```bash
git clone <your-repo-url>
cd tshirt_mockup
```

### 2. ساخت محیط مجازی
```bash
python -m venv venv

# فعال‌سازی:
# Windows (Git Bash):
source venv/Scripts/activate

# Mac/Linux:
source venv/bin/activate
```

### 3. نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```

### 4. اجرای Migrations
```bash
python manage.py migrate
```

### 5. آماده‌سازی تصاویر تیشرت

تصاویر پایه تیشرت را در پوشه زیر قرار دهید:
```
mockups/tshirts/
├── black.png
├── white.png
├── blue.png
└── yellow.png
```

## ▶️ اجرای پروژه

برای اجرای پروژه به **3 ترمینال** نیاز دارید:

### ترمینال 1: Redis Server
```bash
redis-server --port 6380 --slaveof 127.0.0.1 6379
```

### ترمینال 2: Django Development Server
```bash
python manage.py runserver
```

### ترمینال 3: Celery Worker
```bash
# Windows (Git Bash):
celery -A config worker --loglevel=info --pool=solo

# Mac/Linux:
celery -A config worker --loglevel=info
```

سرور Django در آدرس `http://127.0.0.1:8000/` در دسترس خواهد بود.

## 📡 API Endpoints

### 1. تولید موکاپ جدید

**درخواست:**
```http
POST /api/v1/mockups/generate/
Content-Type: application/json

{
  "text": "Hello World"
}
```

**پاسخ:**
```json
{
  "task_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "PENDING",
  "message": "ساخت تصویر آغاز شد"
}
```

---

### 2. بررسی وضعیت تسک

**درخواست:**
```http
GET /api/v1/tasks/{task_id}/
```

**پاسخ:**
```json
{
  "task_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "SUCCESS",
  "results": [
    {
      "id": 1,
      "shirt_color": "black",
      "image_url": "http://127.0.0.1:8000/media/mockups/mockup_123_black.png",
      "created_at": "2024-12-03T15:35:01Z"
    },
    ...
  ]
}
```

**وضعیت‌های ممکن:**
- `PENDING` - در صف انتظار
- `PROCESSING` - در حال پردازش
- `SUCCESS` - تکمیل شده
- `FAILURE` - خطا

---

### 3. لیست تمام موکاپ‌ها

**درخواست:**
```http
GET /api/mockups/
```

**پاسخ:**
```json
{
  "results": [
    {
      "id": 1,
      "text": "Hello World",
      "image_url": "http://127.0.0.1:8000/media/mockups/mockup_123_black.png",
      "shirt_color": "black",
      "created_at": "2024-12-03T15:35:01Z"
    },
    ...
  ]
}
```

## 🧪 تست با curl

### تولید موکاپ:
```bash
curl -X POST http://127.0.0.1:8000/api/v1/mockups/generate/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello World"}'
```

### بررسی وضعیت:
```bash
curl http://127.0.0.1:8000/api/v1/tasks/{task_id}/
```

### لیست موکاپ‌ها:
```bash
curl http://127.0.0.1:8000/api/mockups/
```

## 📁 ساختار پروژه
```
tshirt_mockup/
├── config/              # تنظیمات Django و Celery
│   ├── celery.py
│   ├── settings.py
│   └── urls.py
├── mockups/             # اپلیکیشن اصلی
│   ├── models.py        # مدل‌های Database
│   ├── tasks.py         # تسک‌های Celery
│   ├── views.py         # API Views
│   ├── serializers.py   # DRF Serializers
│   ├── urls.py          # URL routing
│   └── tshirts/         # تصاویر پایه تیشرت
├── media/               # تصاویر تولید شده
├── venv/                # محیط مجازی Python
├── manage.py
├── requirements.txt
└── README.md
```
