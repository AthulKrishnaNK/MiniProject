from django.http import HttpResponseRedirect
from django.shortcuts import render
from orders.models import Orders
from orders.models import Payment
from django.db.models import Sum
from product.models import Product
# from product.models import Product
import datetime

# Create your views here.
def vieworders(request):

    ob = Orders.objects.filter(status="ordered")
    context = {
        'obval':ob,
    }
    return render(request,'orders/VIEW order.html',context)


def place(request,idd):
    obj = Orders.objects.get(o_id=idd)
    if request.method=="POST":
        obj.address=request.POST.get('add')
        obj.save()
        return HttpResponseRedirect('/orders/order/')
    return render(request,'orders/placeorder.html')

def viewordersadmin(request):
    xc = request.session["uid"]
    ob = Orders.objects.filter(v_id=xc,status='ordered')
    context = {
        'obval':ob,
    }
    return render(request,'orders/VIEW order.html',context)

def paye(request):
    ss=request.session["uid"]
    bk=Orders.objects.filter(status="ordered",v_id=ss).aggregate(Sum('total'))['total__sum']
    print(bk)
    context={
        'ok':bk
    }
    if request.method=="POST":
        obj=Payment()
        obj.status="success"
        obj.card_no=request.POST.get('cn')
        obj.total=request.POST.get('t')
        obj.date=datetime.datetime.today()
        obj.cart_id="1"
        obj.cvv=request.POST.get('cv')
        obj.exp_date=request.POST.get('mobileno')
        # ob.exp_date
        obj.holder_name=request.POST.get('acn')
        obj.save()

        objj=Orders.objects.filter(status="ordered")

        for o in objj:
            pobj=Product.objects.get(p_id=o.p_id)
            pobj.quantity=int(pobj.quantity)-int(o.quantity)
            # print(o.quantity)
            # print(type(o.quantity))
            # pobj.quantity=pobj.quantity-o.quantity
            # pobj.save()
            pobj.save()
            o.status="paid"

            o.save()
        return vieworder(request)


    return render(request,'orders/paymnt.html',context)

def vieworder(request):
    ss = request.session["uid"]
    print(ss)
    obj=Orders.objects.filter(v_id=ss,status='paid')
    print(len(obj))
    context={
        'obval':obj
    }
    return render(request,'orders/vieworder.html',context)