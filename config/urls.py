from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # پنل ادمین Django
    path('admin/', admin.site.urls),
    
    # API های ما
    path('api/v1/', include('mockups.urls')),
]

# سرو کردن media files در حالت development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)