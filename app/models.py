from django.db import models

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Produk(models.Model):
    judul = models.CharField(max_length=100)
    gambar = models.ImageField(null=True)
    harga  = models.IntegerField() 
    deskripsi = models.TextField(null=True)
    kategori_produk = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    nama_anda_sesuai_akun = models.CharField(max_length=100, null=True)
    nomor_hp_atau_whatsapp  = models.IntegerField(null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.judul