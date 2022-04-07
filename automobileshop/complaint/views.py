from django.shortcuts import render
from complaint.models import Complaint

# Create your views here.
def viewcompl(request):
    ob = Complaint.objects.all()
    context = {
        'obval':ob,
    }
    return render(request,'complaint/view complaint.html',context)


def viewforward(request):
    ob = Complaint.objects.all()
    context = {
        'obvals':ob,
    }
    return render(request,'complaint/view forwarded complaint and reply.html',context)