# Generated by Django 3.1.3 on 2020-11-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201127_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='produk',
            name='gambar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='produk',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
