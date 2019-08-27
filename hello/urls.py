
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstapp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('admin/', admin.site.urls),
    path('about/', views.about, name="about"),
    path('contacts/', views.contacts, name="contacts")
]
