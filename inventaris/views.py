from django.shortcuts import render, redirect
from django.http import HttpResponse
from inventaris import models
from inventaris import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from inventaris import resource


def index(request):
    barang = models.Barang.objects.all()
    supplier = models.Supplier.objects.all()

    konteks = {
        'barang': barang,
        'supplier': supplier,
    }
    return render(request, 'index.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun berhasil dibuat")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi Kesalahan")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form': form,
        }
    return render(request, 'signup.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def barang(request):
    items = models.Barang.objects.all()

    if request.POST:
        form = forms.FormBarang(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = forms.FormBarang()
            messages.success(request, "Data berhasil disimpan!")

            konteks = {
                'form': form,
                'barangs': items,
            }
            return render(request, 'barang.html', konteks)
            return redirect('barang')
            return HttpResponse.closed(True)
    else:
        form = forms.FormBarang()
        konteks = {
            'form': form,
            'barangs': items,
        }
    return render(request, 'barang.html', konteks)
    return redirect('barang')
    return HttpResponse.closed(True)


def ubah_barang(request, id_barang):
    barang_id = models.Barang.objects.get(id=id_barang)
    template = 'ubah-barang.html'
    if request.POST:
        form = forms.FormBarang(
            request.POST, request.FILES, instance=barang_id)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('barang')
            # return redirect('ubah_barang', id_barang=id_barang)
    else:
        form = forms.FormBarang(instance=barang_id)
        konteks = {
            'form': form,
            'barang_id': barang_id,
        }
    return render(request, template, konteks)


def hapus_barang(request, id_barang):
    barang = models.Barang.objects.filter(id=id_barang)
    barang.delete()

    messages.success(request, "Data berhasil dihapus")
    return redirect('barang')

# def tambah_barang(request):
#     if request.POST:
#         form = forms.FormBarang(request.POST)
#         if form.is_valid():
#             form.save()
#             form = forms.FormBarang()
#             pesan = "Data berhasil disimpan!"

#             konteks = {
#                 'form': form,
#             }
#             return render(request, 'barang.html', konteks)
#     else:
#         form = forms.FormBarang()

#         konteks = {
#             'form': form,
#         }

#     return render(request, 'barang.html', konteks)


def supplier(request):
    items = models.Supplier.objects.all()

    if request.POST:
        form = forms.FormSupplier(request.POST)
        if form.is_valid():
            form.save()
            form = forms.FormSupplier()
            messages.success(request, "Data berhasil disimpan!")

            konteks = {
                'form': form,
                'suppliers': items,
            }
            return render(request, 'supplier.html', konteks)
            return redirect('supplier')
            return HttpResponse.closed(True)
    else:
        form = forms.FormSupplier()
        konteks = {
            'form': form,
            'suppliers': items,
        }
    return render(request, 'supplier.html', konteks)
    return redirect('supplier')
    return HttpResponse.closed(True)


def ubah_supplier(request, id_supplier):
    supplier_id = models.Supplier.objects.get(id=id_supplier)
    template = 'ubah-supplier.html'
    if request.POST:
        form = forms.FormSupplier(request.POST, instance=supplier_id)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('supplier')
            # return redirect('ubah_supplier', id_supplier=id_supplier)
    else:
        form = forms.FormSupplier(instance=supplier_id)
        konteks = {
            'form': form,
            'supplier_id': supplier_id,
        }
    return render(request, template, konteks)


def hapus_supplier(request, id_supplier):
    supplier = models.Supplier.objects.filter(id=id_supplier)
    supplier.delete()

    messages.success(request, "Data berhasil dihapus")
    return redirect('supplier')


def export_xlsx(request):
    barang = resource.BarangResource()
    dataset = barang.export()
    response = HttpResponse(
        dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="report_barang.xlsx"'
    return response
