from django.contrib import admin
from django.urls import path
from .views import test,start_scrape

urlpatterns = [
    path('start_scrape/<str:username>', start_scrape,name="start"),
    path('',test,name="test"),
]