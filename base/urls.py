from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, DeleteView, CustomLoginView, RegisterPage, mark_completed
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.Home, name='home'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('tasks', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
     path('task/<int:task_id>/mark_completed/', mark_completed, name='mark_completed')


]
