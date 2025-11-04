from django.db import models
import uuid


class MockupTask(models.Model):
    """
    مدل اصلی برای ذخیره اطلاعات هر درخواست کاربر
    """

    task_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text="شناسه یونیک تسک"
    )

    text = models.TextField(
        help_text="متنی که کاربر می‌خواد روی تیشرت چاپ بشه"
    )

    status = models.CharField(
        max_length=20,
        default='PENDING',
        choices=[
            ('PENDING', 'در انتظار'),
            ('PROCESSING', 'در حال پردازش'),
            ('SUCCESS', 'موفق'),
            ('FAILURE', 'خطا'),
        ],
        help_text="وضعیت فعلی تسک"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="زمان ایجاد"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="زمان آخرین بروزرسانی"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'تسک موکاپ'
        verbose_name_plural = 'تسک‌های موکاپ'

    def __str__(self):
        return f"{self.task_id} - {self.text[:30]}"


class MockupImage(models.Model):
    """
    مدل برای ذخیره تصاویر تولید شده
    هر تسک می‌تونه 4 تصویر داشته باشه (یکی برای هر رنگ)
    """

    task = models.ForeignKey(
        MockupTask,
        related_name='images',
        on_delete=models.CASCADE,
        help_text="تسک مربوطه"
    )

    shirt_color = models.CharField(
        max_length=20,
        choices=[
            ('black', 'مشکی'),
            ('white', 'سفید'),
            ('blue', 'آبی'),
            ('yellow', 'زرد'),
        ],
        help_text="رنگ تیشرت"
    )

    image = models.ImageField(
        upload_to='mockups/',
        help_text="فایل تصویر تولید شده"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="زمان تولید"
    )

    class Meta:
        ordering = ['shirt_color']
        verbose_name = 'تصویر موکاپ'
        verbose_name_plural = 'تصاویر موکاپ'

    def __str__(self):
        return f"{self.shirt_color} - {self.task.text[:20]}"