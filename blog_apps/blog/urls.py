from django.urls import path

from  .views import BlogPageView,BlogDescView

urlpatterns = [
    path('',BlogPageView.as_view(),name='blog'),
    path('(?P<pk>\d+)$',BlogDescView.as_view(),name='blogdesc'),
]
