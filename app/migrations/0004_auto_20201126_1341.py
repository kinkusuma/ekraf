# Generated by Django 3.1.3 on 2020-11-26 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201126_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produk',
            old_name='kategori_id',
            new_name='kategori_produk',
        ),
    ]