from mahasiswa.models import Mahasiswa, Mahadosen
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
import json, csv, re


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
    

def insert(request):
    
    if request.method == 'POST':        
        for row in request.FILES['docfile']:
            data = str(row)                        
            data = data.strip("b'")
            data = data.strip("\\r\\n")            
            data = list(data.split(","))
            

                        
    return render(request, 'base/mahasiswa/mahasiswa_index.html', {'data':data}) #{'data_pond': data_pond, 'data_site': data_site, 'form': PondCreateForm()}

    