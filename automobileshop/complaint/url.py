from django.conf.urls import url
from complaint import views

urlpatterns=[
    url('viewcom/',views.viewcompl),
    url('viewforw/',views.viewforward),
]