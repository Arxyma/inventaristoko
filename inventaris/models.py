from django.db import models


class Supplier(models.Model):
    nama_supplier = models.CharField(max_length=30)
    alamat = models.TextField()
    lama_kontrak = models.IntegerField()

    def __str__(self):
        return self.nama_supplier


class Barang(models.Model):
    # kodeBarang = models.
    nama_barang = models.CharField(max_length=50)
    harga_beli = models.IntegerField()
    harga_jual = models.IntegerField(null=True)
    jumlah_stok = models.IntegerField()
    id_supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=True)
    img_produk = models.ImageField(upload_to='img_produk/', null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama_barang
