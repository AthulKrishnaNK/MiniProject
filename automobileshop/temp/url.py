from django.conf.urls import url
from temp import views
urlpatterns=[
    url('admin/',views.admin),
    url('vendor/',views.vendor),
    url('user/',views.user),
]