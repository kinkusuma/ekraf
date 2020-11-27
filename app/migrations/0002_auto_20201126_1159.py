# Generated by Django 3.1.3 on 2020-11-26 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='produk',
            name='kategori',
        ),
        migrations.AlterField(
            model_name='produk',
            name='judul',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='produk',
            name='kategori_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.kategori'),
        ),
    ]
