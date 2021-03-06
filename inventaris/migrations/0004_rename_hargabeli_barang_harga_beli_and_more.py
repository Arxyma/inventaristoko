# Generated by Django 4.0.4 on 2022-06-01 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventaris', '0003_rename_hargabarang_barang_hargabeli_barang_hargajual'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barang',
            old_name='hargaBeli',
            new_name='harga_beli',
        ),
        migrations.RenameField(
            model_name='barang',
            old_name='hargaJual',
            new_name='harga_jual',
        ),
        migrations.RenameField(
            model_name='barang',
            old_name='idSupplier',
            new_name='id_supplier',
        ),
        migrations.RenameField(
            model_name='barang',
            old_name='jumlahStok',
            new_name='jumlah_stok',
        ),
        migrations.RenameField(
            model_name='barang',
            old_name='namaBarang',
            new_name='nama_barang',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='lamaKontrak',
            new_name='lama_kontrak',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='namaSupplier',
            new_name='nama_supplier',
        ),
    ]
