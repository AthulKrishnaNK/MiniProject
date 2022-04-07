from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from vendor.models import Vendor
from login.models import Login
# Create your views here.

def vreg(request):
    if request.method == "POST":
        ob = Vendor()
        # ob.name = request.POST.get('vname')
        ob.name = request.POST.get('name')
        ob.email = request.POST.get('email')
        ob.address = request.POST.get('address')
        # ob.image = request.POST.get('img')
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.image = myfile.name
        ob.phone = request.POST.get('mobileno')
        ob.password = request.POST.get('password')
        ob.status = "pending"
        ob.save()
        obj=Login()
        obj.username=request.POST.get('email')
        obj.password=request.POST.get('password')
        obj.type='vendor'
        obj.user_id=ob.v_id
        obj.save()

    return render(request,'vendor/register vendor.html')


def viewven(request):
    ob = Vendor.objects.all()
    context = {
        'obval':ob,
    }
    return render(request,'vendor/verify vendor.html',context)

def acc(request,idd):
    obj=Vendor.objects.get(v_id=idd)
    obj.status='Approved'
    obj.save()
    return viewven(request)



def rej(request,idd):
    obj=Vendor.objects.get(v_id=idd)
    obj.status='Rejected'
    obj.save()
    return viewven(request)
