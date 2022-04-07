from django.http import HttpResponseRedirect
from django.shortcuts import render
from product.models import Product
from orders.models import Orders
from django.core.files.storage import FileSystemStorage
import datetime
# Create your views here.

def addproduct(request):
    ss=request.session["uid"]
    if request.method == "POST":
        ob= Product()
        ob.name = request.POST.get('pname')
        ob.vehiclename = request.POST.get('vname')
        ob.companyname = request.POST.get('cname')
        ob.spare_name = request.POST.get('sname')
        ob.wholesale_price = request.POST.get('wholeprice')
        ob.quantity = request.POST.get('quantity')
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.img = myfile.name
        # ob.img=request.POST.get('image')
        # ob.img = '1'
        ob.retail_price = request.POST.get('retail')
        ob.description = request.POST.get('discription')
        ob.v_id = ss
        ob.save()
        return HttpResponseRedirect('/product/managepro/')

    return render(request,'product/add product with img.html')


def viewproducts(request):
    ob = Product.objects.all()
    context = {
        'obval':ob,
    }
    return render(request,'product/view products.html',context)
from django.http import HttpResponseRedirect
def managepro(request):
    ss = request.session["uid"]
    ob = Product.objects.filter(v_id=ss)
    context = {
        'obvals':ob,
    }
    if request.method=="POST":
        return HttpResponseRedirect('/product/addpro/')

    return render(request,'product/manage product.html',context)


def dele(request,idd):
    obj=Product.objects.get(p_id=idd)
    obj.delete()
    return managepro(request)
def update(request,idd):
    ss=request.session["uid"]
    ob=Product.objects.get(p_id=idd)
    context={
        'ok':ob
    }
    if request.method=="POST":
        ob.name = request.POST.get('pname')
        ob.vehiclename = request.POST.get('vname')
        ob.companyname = request.POST.get('cname')
        ob.spare_name = request.POST.get('sname')
        ob.wholesale_price = request.POST.get('wholeprice')
        ob.quantity = request.POST.get('quantity')

        # ob.img=request.POST.get('image')
        # ob.img = '1'
        ob.retail_price = request.POST.get('retail')
        ob.description = request.POST.get('discription')
        ob.v_id = ss
        ob.save()
        return managepro(request)
    return render(request,'product/update.html',context)
def search(request):
    pr=request.POST.get('pn')
    if request.method=="POST":
        obj=Product.objects.filter(name__icontains=pr)
        context={
            'obval':obj,
        }
        return render(request, 'product/view products.html', context)
    else:
        obj = Product.objects.all()
        context = {
            'obval': obj,
        }
        return render(request,'product/view products.html',context)
    return render(request,'product/view products.html')

def productviewq(request,idd):
    cc=request.session["uid"]

    obj=Product.objects.get(p_id=idd)
    ac=obj.retail_price
    context={
        'ok':obj
    }

    if request.method=="POST":
        objj=Orders()
        objj.status="ordered"
        objj.p_id=idd
        objj.v_id =cc
        objj.address=request.POST.get('sname')
        bc=request.POST.get('qn')
        vc=int(ac)*int(bc)
        objj.total =vc
        objj.quantity =request.POST.get('qn')

        objj.date =datetime.datetime.today()
        objj.time =datetime.datetime.now()
        objj.save()
        return HttpResponseRedirect('/product/search/')
    return render(request,'product/viewproductquanity.html',context)



def buy(request,idd):
    if request.method == "POST":
        ob= Orders()
        ob.address = request.POST.get('address')
        ob.quantity = request.POST.get('quantity')
        ob.date = datetime.date.today()
        ob.time = datetime.datetime.now()
        ob.status = "pending"
        ob.v_id = "1"
        ob.address="pending"

        obj = Product.objects.get(p_id=idd)
        pr = obj.p_id
        ob.p_id = pr
        ob.save()

    return render(request,'product/buy.html')