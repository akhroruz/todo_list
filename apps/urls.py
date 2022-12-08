from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.views import TaskList, TaskDetail, CreateTask, UpdateTask, CustomDeleteView, CustomLoginView, RegisterPage

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('tasks', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('task-create', CreateTask.as_view(), name='task-create'),
    path('task-update/<int:pk>', UpdateTask.as_view(), name='task-update'),
    path('task-delete/<int:pk>', CustomDeleteView.as_view(), name='task-delete'),
]
