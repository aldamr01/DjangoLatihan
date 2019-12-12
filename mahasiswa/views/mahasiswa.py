from mahasiswa.models import Mahasiswa, Mahadosen
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
from collections import namedtuple
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
    class Data:
        def __init__(self, baris1, baris2, baris3)  :
            self.baris1 = baris1
            self.baris2 = baris2
            self.baris3 = baris3

    data_jadi = []          
    datax_jadi = [] 
    datay = []         
    if request.method == 'POST':        
        for row in request.FILES['docfile']:
            data = str(row)                        
            data = data.strip("b'")
            data = data.strip("rn")            
            data = list(data.split(","))
            temp = {"baris1":data[0],"baris2":data[1],"baris3":data[2].strip('\\r\\')}
            datay.append({"s1":data[0],"s2":data[1],"s3":data[2].strip('\\r\\')}) #Cara 1
            data_jadi.append(namedtuple("Data", temp.keys())(*temp.values())) #Cara 2
            datax_jadi.append(Data(data[0],data[1],data[2].strip('\\r\\'))) #Cara 3 gagal


    # print(data_jadi)
    # print("datax_jadi = "+str(type(datax_jadi[1])))
    # print("data_jadi  = "+str(type(data_jadi[1])))

    return render(request, 'base/mahasiswa/mahasiswa_index.html', {'data':datay}) #{'data_pond': data_pond, 'data_site': data_site, 'form': PondCreateForm()}

    