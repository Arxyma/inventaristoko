from import_export import resources
from inventaris import models
from import_export import fields


class BarangResource(resources.ModelResource):
    nama_supplier = fields.Field(
        attribute='id_supplier', column_name='nama_supplier')

    class Meta:
        model = models.Barang
        fields = ['nama_barang', 'harga_beli', 'harga_jual',
                  'jumlah_stok', 'nama_supplier', 'tanggal']
        export_order = ['nama_barang', 'harga_beli', 'harga_jual',
                        'jumlah_stok', 'nama_supplier', 'tanggal']
