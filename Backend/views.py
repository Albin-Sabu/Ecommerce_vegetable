from django.shortcuts import render, redirect
from Backend.models import categorydb
from Backend.models import productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Webapp.models import contactdb
from django.contrib import messages


# Create your views here.

def index_page(request):
    return render(request, "index.html")


def add_category(request):
    return render(request, "add_category.html")


def category(request):
    if request.method == "POST":
        a = request.POST.get('cname')
        b = request.POST.get('des')
        c = request.FILES['image']
        obj1 = categorydb(Cname=a, Des=b, Image=c)
        obj1.save()
        messages.success(request,'Category Added Successfully!')
        return redirect(add_category)


def disp(request):
    data = categorydb.objects.all()
    return render(request, "disp_category.html", {'data': data})


def edit_cat(request, cid):
    data = categorydb.objects.get(id=cid)
    return render(request, "edit.html", {'data': data})


def update_cat(request, cid):
    if request.method == "POST":
        a = request.POST.get('cname')
        b = request.POST.get('des')
        try:
            c = request.FILES['image']
            fs = FileSystemStorage()
            files = fs.save(c.name, c)
        except MultiValueDictKeyError:
            files = categorydb.objects.get(id=cid).Image
        categorydb.objects.filter(id=cid).update(Cname=a, Des=b, Image=files)
        messages.success(request,'Edited Successfully...')
        return redirect(disp)


def delete_cat(request, cid):
    data = categorydb.objects.filter(id=cid)
    data.delete()
    messages.error(request,'Deleted.....')
    return redirect(disp)


def login_page(request):
    return render(request, "login.html")


def admin_login(request):
    if request.method == "POST":
        a = request.POST.get('username')
        b = request.POST.get('pass')
        if User.objects.filter(username__contains=a).exists():
            x = authenticate(username=a, password=b)
            if x is not None:
                login(request, x)
                request.session['username'] = a
                request.session['password'] = b
                messages.success(request,'WELCOME...')
                return redirect(index_page)
            else:
                messages.warning(request, 'Invalid Username or Password...')
                return redirect(login_page)
        else:
            messages.error(request, 'Username not found...')
            return redirect(login_page)


def sign_out(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, 'THANK YOU...')
    return redirect(login_page)


def product_page(request):
    cat = categorydb.objects.all()
    return render(request, "product.html", {'cat': cat})


def product_reg(request):
    if request.method == "POST":
        a = request.POST.get('category')
        b = request.POST.get('pname')
        c = request.POST.get('description')
        d = request.POST.get('price')
        e = request.FILES['pimage']
        obj1 = productdb(Category=a, Pname=b, Description=c, Price=d, Pimage=e)
        obj1.save()
        messages.success(request, 'Category Added Successfully!')
        return redirect(product_page)


def disp_p(request):
    data = productdb.objects.all()
    return render(request, "disp_product.html", {'data': data})


def edit_p(request, pid):
    data = productdb.objects.get(id=pid)
    cat = categorydb.objects.all()
    return render(request, "edit_p.html", {'data': data, 'cat': cat})


def update_pd(request, pid):
    if request.method == "POST":
        a = request.POST.get('category')
        b = request.POST.get('pname')
        c = request.POST.get('description')
        d = request.POST.get('price')
        try:
            e = request.FILES['pimage']
            fs = FileSystemStorage()
            files = fs.save(e.name, e)
        except MultiValueDictKeyError:
            files = productdb.objects.get(id=pid).Pimage
        productdb.objects.filter(id=pid).update(Category=a, Pname=b, Description=c, Price=d, Pimage=files)
        messages.success(request, 'Edited Successfully...')
        return redirect(disp_p)


def delete_pd(request, pid):
    data = productdb.objects.filter(id=pid)
    data.delete()
    messages.error(request, 'Deleted.....')
    return redirect(disp_p)


def contact_details(request):
    data = contactdb.objects.all()
    return render(request, "contact_data.html", {'data': data})


def delete_contact(request, cid):
    data = contactdb.objects.filter(id=cid)
    data.delete()
    return redirect(contact_details)
