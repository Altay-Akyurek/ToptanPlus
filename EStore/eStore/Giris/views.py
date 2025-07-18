from django.shortcuts import render,redirect,get_object_or_404
from .models import Product  # Product modelini import et!
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

def store_home(request):
    products = Product.objects.all()  # products değişkenini tanımla
    return render(request, "store/home.html", {"products": products})

#Üyelik sistemi
#register open

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('store_home')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html', {'from':form})

#giriş yapma protokolü
#login open proto.

def login_view(request):
    if request.method== 'POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid:
            user= form.get_user()
            login(request,user)
            return redirect('store_home')
    else:
        form=AuthenticationForm()
    return render(request,'registraion/login.html',{'form':form})

#cıkış yapma
#logout open

def logout_view(request):
    logout(request)
    return redirect('store_home')


#kart ödemesi
#cart pay
@login_required
def  cart_view(request):
    cart=request.session.get('cart',{})
    product=Product.objects.filter(id_in=cart.keys())
    cart_items=[]
    for product in product:
        cart_items.append({
        'product':product,
        'quantity':cart[str(product.id)]})

    return render(request,'store/cart.html',{'cart_items':cart_items})

@login_required

def add_to_cart(request,product_id):
    cart=request.session.get('cart',{})
    cart[str(product_id)]=cart.get(str(product_id),0)+1
    request.session['cart']=cart
    return redirect('cart')

#hakımızda bölümü
#Abount Page
def about_view(request):
    return render(request,"store/about.html")