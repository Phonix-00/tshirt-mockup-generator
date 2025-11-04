from rest_framework import serializers
from .models import MockupTask, MockupImage


class MockupImageSerializer(serializers.ModelSerializer):
    """
    Serializer برای تبدیل MockupImage به JSON

    این serializer اطلاعات تصاویر تولید شده رو به فرمت JSON برمی‌گردونه
    """

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = MockupImage
        fields = ['id', 'shirt_color', 'image_url', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get_image_url(self, obj):
        """
        ساخت URL کامل برای تصویر

        به جای: "mockups/image.png"
        برمی‌گردونه: "http://127.0.0.1:8000/media/mockups/image.png"
        """
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class MockupTaskSerializer(serializers.ModelSerializer):
    """
    Serializer برای تبدیل MockupTask به JSON

    این serializer اطلاعات تسک و تصاویر مربوطه رو برمی‌گردونه
    """

    images = MockupImageSerializer(many=True, read_only=True)

    class Meta:
        model = MockupTask
        fields = ['task_id', 'text', 'status', 'images', 'created_at', 'updated_at']
        read_only_fields = ['task_id', 'status', 'created_at', 'updated_at']


class GenerateInputSerializer(serializers.Serializer):
    """
    Serializer برای ولیدیت کردن ورودی API تولید موکاپ

    فقط چک می‌کنه که ورودی کاربر درست باشه
    """

    text = serializers.CharField(
        required=True,
        max_length=500,
        min_length=1,
        help_text="متنی که روی تیشرت چاپ می‌شه",
        error_messages={
            'required': 'فیلد text الزامی است',
            'blank': 'متن نمی‌تواند خالی باشد',
            'max_length': 'متن نمی‌تواند بیشتر از 500 کاراکتر باشد',
            'min_length': 'متن نمی‌تواند کمتر از 1 کاراکتر باشد',
        }
    )

    def validate_text(self, value):
        """
        اعتبارسنجی اضافی برای متن
        """
        # حذف فضاهای خالی اضافی
        value = value.strip()

        # چک کردن که فقط فضای خالی نباشه
        if not value:
            raise serializers.ValidationError("متن نمی‌تواند فقط فضای خالی باشد")

        return value