from django.conf.urls import url
from product import views

urlpatterns=[
    url('addpro/',views.addproduct),
    url('viewpro/',views.viewproducts),
    url('managepro/',views.managepro),
    url('search/',views.search),
    url('buy/(?P<idd>\w+)', views.buy, name='buy'),
    url('prq/(?P<idd>\w+)',views.productviewq,name="viewp"),
    url('delete/(?P<idd>\w+)',views.dele,name='delp'),
    url('edit/(?P<idd>\w+)',views.update,name="uppro")

]