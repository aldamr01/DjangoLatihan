from contoh1.views import mahasiswa
from django.urls import path, include

urlpatterns = [
    path('', mahasiswa.index),
    path('create', mahasiswa.create),
]