
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.task_list, name='task-list'),
    path('add/', views.add_task, name='add-task'),
    path('edit/<int:pk>/', views.edit_task, name='edit-task'),
    path('delete/<int:pk>/', views.delete_task, name='delete-task'),

]
