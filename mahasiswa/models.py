from django.db import models

# Create your models here.
class Mahadosen(models.Model):
    nama = models.CharField(null=False, default=None, max_length=100)


class Mahasiswa(models.Model):
    class Meta:
        db_table = "mahasiswa"
    
    id = models.AutoField(primary_key=True)
    nama = models.CharField(null=False, default=None, max_length=100)
    mahadosen = models.ForeignKey(Mahadosen, on_delete=models.PROTECT)