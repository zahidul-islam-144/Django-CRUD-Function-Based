from django.contrib import admin
from django.urls import path, include
from App_Enroll import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('display/', views.add_display, name='display'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('edit/<int:id>/', views.edit_student, name='edit'),
    path('', views.add_display, name='display'),
]
