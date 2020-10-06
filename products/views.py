from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.views import View
from django.contrib import messages
# Create your views here.

def home(request):
    products=Product.objects.all()
    services=Service.objects.all()
    context={
        'products':products,
        'services':services,
    }
    return render(request,'home.html',context)

def product_details(request,id):
    product=get_object_or_404(Product,pk=id)
    context={
        'product':product,
    }
    print(product.title)
    return render(request,'detail.html',context)

def about_us(request):
    team=Team.objects.all()
    about=About_us.objects.get(title__icontains='Best-Products')
    services=Service.objects.all()
    context={
        "about":about,
        'members':team,
        'services':services,

    }
    return render(request,'about.html',context)

def our_services(request):
    services=Service.objects.all()
    context={
        'services':services,
    }
    return render(request,"services.html",context)

def search(request):
    n=request.GET["search"]

    return redirect(f"https://www.amazon.com/s?k={n}&tag=codermiki-20")

def contactView(request):
    if request.method=="GET":
        contact=Contact.objects.all()
        team=Team.objects.all()
        about=About_us.objects.get(title__icontains='Best-Products')
        context={
            "contact":contact,
            'members':team,
            "about":about,
        }
        return render(request,"contact.html",context)
    if request.method=="POST":
        print(request.POST)
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        message=request.POST['message']
        if name!='' and phone!=''and email!=''and message!='':
           msg=Messages.objects.create(name=name,phone_number=phone,email=email,message=message)
           print(" this was a good data and was save")
           messages.info(request,f"Dr  {request.user} Your Notes was Saved successfully ")
        else:
            print("his was not good data and was not save")
            messages.info(request,f"Dr  {request.user} please fill all the fields currectly before submiting the form ")
        return redirect("products:contact")