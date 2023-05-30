from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Order
from .models import Feedback
from django.db.models import Sum
import datetime

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'aboutus.html')

def contact_page(request):
    return render (request,'contact_us.html')
    
def contact(request):
    name= request.POST.get('name')
    feedback= request.POST.get('feedback')
    date = datetime.datetime.now()

    myfeedback=Feedback(
        name=name,
        feedback=feedback,
        date=str(date)
    )
    myfeedback.save()
    return render(request,'contact_us.html')


def search(request):
    try:
        sc=request.POST.get('search')
        
        sc=Product.objects.get(product_name=sc)

        params={'srch':sc}
        return render(request,'search.html',params)
    except:
        return render(request,'search.html')
    
    
def productview(request):
    products=Product.objects.all()
    params={'product':products}
    return render(request,'items.html',params)


def cart(request):
    order=Order.objects.all()

    total_price=Order.objects.aggregate(Sum('price'))
    total_price=total_price.get('price__sum')
    
    params={'order':order,'total_price':total_price}
    return render(request,'cart.html',params)

def order(request,product_id):

    order=Product.objects.get(product_id=product_id)
    
    myorder=Order(product_id=order.product_id,
                  product_name=order.product_name,
                  category=order.category,
                  subcategory=order.subcategory,
                  price=order.price,
                  desc=order.desc,
                  pub_date=order.pub_date
                  )
    myorder.save()
    products=Product.objects.all()
    
   
    params={'product':products}
    return render(request,'items.html',params)
   

def delete(request,product_id):
    instance = Order.objects.filter(product_id=product_id).first()
    if instance:
        instance.delete()

    order=Order.objects.all()

    total_price=Order.objects.aggregate(Sum('price'))
    total_price=total_price.get('price__sum')
    
    params={'order':order,'total_price':total_price}
    return render(request,'cart.html',params)