# Generated by Django 2.2.7 on 2019-11-30 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contoh1', '0004_remove_mahadosen_alamat'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahasiswa',
            name='mahadosen',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='contoh1.Mahadosen'),
            preserve_default=False,
        ),
    ]