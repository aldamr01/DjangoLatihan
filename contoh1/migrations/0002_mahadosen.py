# Generated by Django 2.2.7 on 2019-11-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contoh1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahadosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]
