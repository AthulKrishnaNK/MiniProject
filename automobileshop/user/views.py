from django.shortcuts import render

from login.models import Login
from user.models import User
# Create your views here.
def user(request):
    if request.method=="POST":
        ob = User()

        ob.name = request.POST.get('name')
        ob.email = request.POST.get('email')
        ob.address = request.POST.get('address')
        ob.phone = request.POST.get('mobileno')


        ob.save()
        obj = Login()
        obj.username = request.POST.get('email')
        obj.password = request.POST.get('password')
        obj.type = 'user'
        obj.user_id = ob.u_id
        obj.save()
    return render(request,'user/userreg.html')