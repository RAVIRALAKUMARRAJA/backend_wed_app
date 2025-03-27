from django.urls import path
from .views import AppListCreateView,admin_dashboard, add_task, edit_task, delete_task, approve_submission, reject_submission

urlpatterns = [
    path("", admin_dashboard, name="admin_dashboard"),
    path('apps/', AppListCreateView.as_view(), name='app-list'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin/task/add/', add_task, name='add_task'),
    path('admin/task/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('admin/task/delete/<int:task_id>/', delete_task, name='delete_task'),
    path('admin/submission/approve/<int:submission_id>/', approve_submission, name='approve_submission'),
    path('admin/submission/reject/<int:submission_id>/', reject_submission, name='reject_submission'),
]

