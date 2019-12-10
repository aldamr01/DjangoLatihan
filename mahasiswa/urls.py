from mahasiswa.views import mahasiswa
from django.urls import path, include

urlpatterns = [
    path('', mahasiswa.insert, name='mahasiswa input'),
    path('create', mahasiswa.create),
]