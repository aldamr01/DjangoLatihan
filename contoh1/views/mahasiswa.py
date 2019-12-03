from contoh1.models import Mahasiswa, Mahadosen
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json


def index(request):
    data_mahasiswa = Mahasiswa.objects.all()
    data = json.loads(serializers.serialize("json", data_mahasiswa))
    return JsonResponse(data, safe=False)


def create(request):
    data = Mahasiswa()
    data.id = 1
    data.nama = "Fatin4"
    data.mahadosen = Mahadosen.objects.get(pk=1)

    if data.save() is True:        
        return JsonResponse({"pesan": "data gagal dimasukan"})        
    else:
        data_mahasiswa = Mahasiswa.objects.all()
        data = json.loads(serializers.serialize("json", data_mahasiswa))
        return JsonResponse(data, safe=False)
    