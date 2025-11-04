from django.urls import path
from .views import GenerateMockupView, TaskStatusView, MockupListView

# نام app برای namespace
app_name = 'mockups'

urlpatterns = [
    # API 1: تولید موکاپ
    # POST /api/v1/mockups/generate/
    path('mockups/generate/', GenerateMockupView.as_view(), name='generate-mockup'),

    # API 2: بررسی وضعیت task
    # GET /api/v1/tasks/<uuid:task_id>/
    path('tasks/<uuid:task_id>/', TaskStatusView.as_view(), name='task-status'),

    # API 3: لیست موکاپ‌ها
    # GET /api/mockups/
    path('mockups/', MockupListView.as_view(), name='mockup-list'),
]