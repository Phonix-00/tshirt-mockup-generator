import os
from celery import Celery

# تنظیم Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# ساخت Celery app
app = Celery('config')

# خواندن تنظیمات از Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# پیدا کردن تسک‌ها به صورت خودکار
app.autodiscover_tasks()