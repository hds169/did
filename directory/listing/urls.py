
from django.conf.urls import url
from .import views

urlpatterns = [
   url(r'^$',views.index, name='index'),
   url(r'^contact$',views.contactss, name='contact'),
   url(r'^article$',views.artikl, name='article'),
   url(r'^link$',views.linkss, name='link'),
]
