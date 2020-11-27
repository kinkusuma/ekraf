from django.contrib import admin
from app.models import Kategori, Produk

# Register your models here.

class DaftarProduk(admin.ModelAdmin):
    list_display = ['judul', 'harga', 'kategori_produk']
    search_fields = ['judul', 'harga', 'kategori_produk']
    list_filter =  ['kategori_produk']
    list_per_page = 5

admin.site.register(Produk, DaftarProduk)
admin.site.register(Kategori)