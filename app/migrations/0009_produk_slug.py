# Generated by Django 3.1.3 on 2020-11-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201127_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='produk',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
