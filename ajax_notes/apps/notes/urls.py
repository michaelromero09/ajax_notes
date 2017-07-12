from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_note$', views.add_note),
    url(r'^delete$', views.delete),
    url(r'^edit$', views.edit),
]