# Generated by Django 3.2.4 on 2021-06-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img/productos/%Y/%m/%d'),
        ),
    ]
