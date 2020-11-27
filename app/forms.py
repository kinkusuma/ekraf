from django.forms import ModelForm
from django import forms
from app.models import Produk
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormProduk(ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'gambar' : forms.ClearableFileInput({'class':'form-control'}),
            'harga' : forms.NumberInput({'class':'form-control'}),
            'deskripsi' : forms.Textarea({'class':'form-control'}),
            'kategori_produk' : forms.Select({'class':'form-control'}),
            'nama_anda_sesuai_akun' : forms.TextInput({'class':'form-control'}),
            'nomor_hp_atau_whatsapp ' : forms.NumberInput({'class':'form-control'}),
        }



class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)

        widgets = {
            'username' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
        }