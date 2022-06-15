from django.forms import ModelForm
from django import forms
from inventaris import models


class FormBarang(ModelForm):
    class Meta:
        model = models.Barang
        fields = '__all__'

        widgets = {
            'nama_barang': forms.TextInput({'class': 'form-control'}),
            'harga_beli': forms.NumberInput({'class': 'form-control'}),
            'harga_jual': forms.NumberInput({'class': 'form-control'}),
            'jumlah_stok': forms.NumberInput({'class': 'form-control'}),
            'id_supplier': forms.Select({'class': 'form-control'}),
        }


class FormSupplier(ModelForm):
    class Meta:
        model = models.Supplier
        fields = '__all__'

        widgets = {
            'nama_supplier': forms.TextInput({'class': 'form-control'}),
            'alamat': forms.TextInput({'class': 'form-control'}),
            'lama_kontrak': forms.NumberInput({'class': 'form-control'}),
        }
