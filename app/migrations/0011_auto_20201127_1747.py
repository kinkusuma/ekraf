# Generated by Django 3.1.3 on 2020-11-27 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_produk_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produk',
            old_name='nomor_hp',
            new_name='nomor_hp_atau_whatsapp',
        ),
    ]