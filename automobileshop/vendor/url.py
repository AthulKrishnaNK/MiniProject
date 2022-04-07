from django.conf.urls import url
from vendor import views
urlpatterns=[
    url('vendorreg/',views.vreg),
    url('viewvendor',views.viewven),
    url('app/(?P<idd>\w+)',views.acc,name="apv"),
    url('rej/(?P<idd>\w+)', views.rej, name="rejv")

]