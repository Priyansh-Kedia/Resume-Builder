from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'builder'

urlpatterns = [
    path('', views.index),

    path('update_profile', views.update_profile, name='update_profile')
]