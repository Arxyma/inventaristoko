"""inventaristoko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from inventaris import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('barang/', views.barang, name='barang'),
    path('barang/ubah/<int:id_barang>', views.ubah_barang, name='ubah_barang'),
    path('barang/hapus/<int:id_barang>',
         views.hapus_barang, name="hapus_barang"),
    path('supplier/', views.supplier, name='supplier'),
    path('supplier/ubah/<int:id_supplier>',
         views.ubah_supplier, name='ubah_supplier'),
    path('supplier/hapus/<int:id_supplier>',
         views.hapus_supplier, name="hapus_supplier"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('export/xlsx/', views.export_xlsx, name='export_xlsx'),
    # path('tambah-barang/', views.tambah_barang),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
