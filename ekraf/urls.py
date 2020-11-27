"""ekraf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('nasdboiheaianciaegr9237buw/', admin.site.urls),
    path('', index, name='index'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='index'), name='keluar'),
    path('daftar/', daftar, name='daftar'),
    path('pengguna/', user, name='user'),
    path('pengguna/tambah-produk/', tambah_produk, name='add-product'),
    path('pengguna/produk/ubah/<int:id_produk>', ubah, name='ubah'),    
    path('pengguna/produk/hapus/<int:id_produk>', hapus, name='hapus'),
    path('pengguna/produk/<pk>', Detail.as_view(), name='detail'),
    path('kategori/animasi', animasi, name='animasi'),
    path('kategori/busana', busana,name='busana'),
    path('kategori/desain-arsitektur', darsi,name='darsi'),
    path('kategori/desain-interior', dinter,name='dinter'),
    path('kategori/desain-komunikasi-visual', dkv,name='dkv'),
    path('kategori/fotografi', fotografi,name='fotografi'),
    path('kategori/kerajinan-tangan',kerajinan ,name='kerajinan'),
    path('kategori/musik',musik ,name='musik'),
    path('kategori/produk-pariwisata',pariwisata ,name='pariwisata'),
    path('kategori/video', video,name='video'),
    path('kategori/seni-murni', seni,name='seni'),
    path('kategori/lainnya', lainnya,name='lainnya'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
