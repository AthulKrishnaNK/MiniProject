from django.shortcuts import render
from login.models import Login

# Create your views here.
def login(request):
    if request.method == "POST":
        un = request.POST.get("u")
        ps = request.POST.get("p")
        print(ps)
        if Login.objects.filter(username=un, password=ps):
            obj = Login.objects.filter(username=un, password=ps)
            tp = ""
            for l in obj:
                tp = l.type
                uid = l.user_id
                if tp == "admin":
                    request.session["uid"] = uid
                    return render(request, 'temp/admin_home.html')
                elif tp == "user":
                    request.session["uid"] = uid
                    return render(request, 'temp/user_home.html')
                elif tp == "vendor":
                    request.session["uid"] = uid
                    return render(request, 'temp/vendor_home.html')
                # elif tp == "user":
                #     request.session["uid"] = uid
                #     return render(request, 'temp/User.html')

        else:
            obje = "Incorrect username or password!!!"
            context = {
                'inv': obje,
            }
            return render(request, 'login/login.html', context)
    return render(request, 'login/login.html')