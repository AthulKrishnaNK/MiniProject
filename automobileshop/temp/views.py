from django.shortcuts import render

# Create your views here.
def user(request):
    return render(request,'temp/user_home.html')
def admin(request):
    return render(request,'temp/admin_home.html')
def vendor(request):
    return render(request,'temp/vendor_home.html')