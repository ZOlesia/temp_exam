from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^quotes$', views.success),
    url(r'^contribute$', views.contribute),
    url(r'^add/(?P<id>\d+)$', views.add),
    url(r'^users/(?P<id>\d+)$', views.show),
]



    # url(r'^books/(?P<id>\d+)$', views.book),
    # url(r'^users/(?P<id>\d+)$', views.user),