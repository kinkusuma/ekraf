from django.shortcuts import redirect,render 
from app.models import Produk
from app.forms import FormProduk, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.views.generic.detail import DetailView 

# Create your views here.

class Detail(DetailView):
    model = Produk
    template_name = 'detail.html'

def index(request):
    produks = Produk.objects.all()

    context = {
        'produks' : produks
    }

    return render(request, 'index.html', context)

def user(request):
    produks = Produk.objects.filter(nama_anda_sesuai_akun = request.user.get_username())

    context = {
        'produks' : produks
    }

    return render(request, 'user.html', context)

def daftar(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pendaftaran berhasil, silahkan masuk keakun anda")
            return redirect('daftar')
        else:
            messages.error(request, "Terjadi kesalahan, data yang dimasukkan tidak valid")
            return redirect('daftar')
    else:
        form = UserCreationForm()

        context = {
            'form' : form
        }

    return render(request, 'signup.html', context)

@login_required(login_url=settings.LOGIN_URL)
def tambah_produk(request):
    if request.POST:
        form = FormProduk(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormProduk()
            return redirect('user')
        else:
            messages.error(request, "Terjadi kesalahan, data yang dimasukkan tidak valid")
            return redirect('add-product')
    else:
        form = FormProduk()

        context = {
            'form' : form,
        }

    return render(request, 'add-product.html', context)

@login_required(login_url=settings.LOGIN_URL)
def ubah(request, id_produk):
    produk = Produk.objects.get(id=id_produk)
    template = 'ubah.html'
    if request.POST:
        form = FormProduk(request.POST, request.FILES, instance=produk)
        if form.is_valid():
            form.save()
            return redirect ('user')
    else:
        form = FormProduk(instance=produk)
        context = {
            'produk' : produk,
            'form' : form
        }

    return render(request, template, context)

@login_required(login_url=settings.LOGIN_URL)
def hapus(request, id_produk):
    produk = Produk.objects.get(id=id_produk)
    produk.delete()

    return redirect('user')

def animasi(request):
    produks = Produk.objects.filter(kategori_produk__nama='animasi')
    namaproduk = "Animasi"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)

def busana(request):
    produks = Produk.objects.filter(kategori_produk__nama='busana')
    namaproduk = "Busana"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)

def darsi(request):
    produks = Produk.objects.filter(kategori_produk__nama='desain arsitektur')
    namaproduk = "Desain Arsitektur"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)

def dinter(request):
    produks = Produk.objects.filter(kategori_produk__nama='desain interior')
    namaproduk = "Desain Interior"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)

def dkv(request):
    produks = Produk.objects.filter(kategori_produk__nama='desain komunikasi visual')
    namaproduk = "DKV"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)


def fotografi(request):
    produks = Produk.objects.filter(kategori_produk__nama='fotografi')
    namaproduk = "Fotografi"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)

def kerajinan(request):
    produks = Produk.objects.filter(kategori_produk__nama='kerajinan tangan')
    namaproduk = "Kerajinan Tangan"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)

def musik(request):
    produks = Produk.objects.filter(kategori_produk__nama='musik')
    namaproduk = "Musik"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)

def pariwisata(request):
    produks = Produk.objects.filter(kategori_produk__nama='produk pariwisata')
    namaproduk = "Pariwisata"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)

def video(request):
    produks = Produk.objects.filter(kategori_produk__nama='video')
    namaproduk = "Video"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)

def seni(request):
    produks = Produk.objects.filter(kategori_produk__nama='seni murni')
    namaproduk = "Seni Murni"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)

def lainnya(request):
    produks = Produk.objects.filter(kategori_produk__nama='lainnya')
    namaproduk = "Lainnya"
    context = {
        'namaproduk' : namaproduk,
        'produks' : produks
    }

    return render(request, 'index.html', context)

