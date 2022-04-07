from django.conf.urls import url
from orders import views
urlpatterns=[
    url('vieworders/',views.vieworders),
    url('buy/(?P<idd>\w+)',views.place,name='place'),
    url('order/',views.viewordersadmin),
    url('payee/',views.paye),
    url('orderv/',views.vieworder)
]