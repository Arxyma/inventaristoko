from django.contrib import admin
from inventaris import models
# Register your models here.


class BarangAdmin(admin.ModelAdmin):
    list_display = ['nama_barang', 'harga_beli', 'harga_jual', 'jumlah_stok']
    search_fields = ['nama_barang', 'harga_beli',
                     'harga_jual', 'jumlah_stok', 'id_supplier']
    list_filter = ['id_supplier']
    list_per_page = 5


admin.site.register(models.Supplier)
admin.site.register(models.Barang, BarangAdmin)
