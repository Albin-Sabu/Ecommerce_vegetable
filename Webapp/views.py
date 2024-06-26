from django.shortcuts import render, redirect
from Backend.models import productdb, categorydb
from Webapp.models import contactdb, logindb, cartdb,shipingdb
from django.contrib import messages
import razorpay

# Create your views here.
def home_page(request):
    cat = categorydb.objects.all()
    return render(request, "home.html", {'cat': cat})


def about_page(request):
    cat = categorydb.objects.all()
    return render(request, "about.html", {'cat': cat})


def contact_page(request):
    cat = categorydb.objects.all()
    return render(request, "contact.html", {'cat': cat})


def save_contact(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('phone')
        c = request.POST.get('email')
        d = request.POST.get('subject')
        e = request.POST.get('message')
        obj = contactdb(Name=a, Phone=b, Email=c, Subject=d, Message=e)
        obj.save()
        return redirect(contact_page)


def cart_page(request):
    cat = categorydb.objects.all()
    return render(request, "cart.html", {'cat': cat})


def product_page(request):
    pro = productdb.objects.all()
    cat = categorydb.objects.all()
    return render(request, "our_products.html", {'pro': pro, 'cat': cat})


def filtered_page(request, cat_name):
    data = productdb.objects.filter(Category=cat_name)
    cat = categorydb.objects.filter(Cname=cat_name)
    return render(request, "products_filtered.html", {'data': data, 'cat': cat})


def single_page(request, pid):
    data = productdb.objects.get(id=pid)
    return render(request, "single_product.html", {'data': data})


def register_page(request):
    return render(request, "register.html")


def register_p(request):
    if request.method == "POST":
        a = request.POST.get('uname')
        b = request.POST.get('emailid')
        c = request.POST.get('passw')
        d = request.POST.get('cpassw')
        obj1 = logindb(Uname=a, Emailid=b, Passw=c, Cpassw=d)
        if logindb.objects.filter(Uname=a).exists():
            messages.warning(request, 'User Already Exists...')
            return redirect(register_page)
        elif logindb.objects.filter(Emailid=b).exists():
            messages.warning(request, 'Email ID Already Exists...')
            return redirect(register_page)
        else:
            messages.success(request, 'Successfully Registered...')
            obj1.save()
        return redirect(logins)


def user(request):
    if request.method == "POST":
        un = request.POST.get('user')
        pa = request.POST.get('password')
        if logindb.objects.filter(Uname=un, Passw=pa).exists():
            request.session['Uname'] = un
            request.session['Passw'] = pa
            messages.success(request, 'WELCOME...')
            return redirect(home_page)
        else:
            messages.warning(request, 'Invalid Username/Password...')
            return redirect(logins)
    else:
        messages.success(request, 'Invalid User...')
        return redirect(logins)


def user_out(request):
    del request.session['Uname']
    del request.session['Passw']
    messages.success(request, 'THANK YOU...')
    return redirect(home_page)


def cartpage(request):
    if request.method == "POST":
        a = request.POST.get('qtyy')
        b = request.POST.get('tot')
        c = request.POST.get('pn')
        d = request.POST.get('use')
        obj1 = cartdb(User=d, Product=c, Quantity=a, Prices=b)
        obj1.save()
        messages.success(request, 'Successfully Added...')
        return redirect(home_page)


def disp_cart(request):
    data = cartdb.objects.filter(User=request.session['Uname'])
    total_price = 0
    shipping_price = 0
    full_total = 0
    for i in data:
        total_price = total_price + i.Prices
        if total_price < 250:
            shipping_price = 45
        else:
            shipping_price = 10
        full_total = shipping_price + total_price

    return render(request, "cartpage.html", {'data': data, 'total_price': total_price, 'shipping_price': shipping_price, 'full_total': full_total})


def logins(request):
    return render(request, "logins.html")


def check_out(request):
    data = cartdb.objects.filter(User=request.session['Uname'])
    total_price = 0
    shipping_price = 0
    full_total = 0
    for i in data:
        total_price = total_price + i.Prices
        if total_price < 250:
            shipping_price = 45
        else:
            shipping_price = 10
        full_total = shipping_price + total_price
    return render(request, "checkout.html",{'data':data, 'total_price': total_price, 'shipping_price': shipping_price, 'full_total': full_total})


def ship_check(request):
    if request.method == "POST":
        a = request.POST.get('use')
        b = request.POST.get('email')
        c = request.POST.get('address')
        d = request.POST.get('phone')
        e = request.POST.get('message')
        f = request.POST.get('price')
        obj1 = shipingdb(User=a, Email=b,Address=c,Phone=d,Message=e, Price=f)
        obj1.save()
        return redirect(payments)

def payments(request):
    customer = shipingdb.objects.order_by('-id').first()

    payy = customer.Price
    amount = int(payy * 100)
    payy_str = str(amount)
    for i in payy_str:
        print(i)

    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('', '')
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})

    return render(request, "payment.html", {'customer': customer, 'payy_str': payy_str})
