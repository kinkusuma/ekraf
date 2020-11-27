# Generated by Django 3.1.3 on 2020-11-26 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=100)),
                ('judul', models.TextField()),
                ('foto', models.ImageField(upload_to='static/uploads/')),
                ('harga', models.IntegerField()),
                ('slug', models.SlugField()),
                ('deskripsi', models.TextField()),
                ('tanggal', models.DateField()),
            ],
        ),
    ]
