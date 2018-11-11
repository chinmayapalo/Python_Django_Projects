from django.urls import path
from django.conf.urls import url

from  .views import BlogPageView,BlogDescView
from . import views

urlpatterns = [
#url(r'^$', views.index, name='index'),
#url(r'^details/(?P<id>\w{0,50})/$',views.details,name='details'),
    url(r'^$',BlogPageView.as_view(),name='blog'),
    url(r'^(?P<id>\d+)/$',views.BlogDescView,name='blogdesc'),
]

