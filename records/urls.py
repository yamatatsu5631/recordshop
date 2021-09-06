from django.contrib import admin
from django.urls import path

from records.views import top

urlpatterns = [
    path('', top, name="top"),
    ]