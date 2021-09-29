# from django.conf.urls import url
# from basic_app import views
#
# #for template tagging, set a variable name-global name and app name
# app_name = 'basic_app'
#
#
# urlpatterns = [
#     url(r'^relative/$', views.relative, name = 'relative'),
#
#     url(r'^other/$', views.other, name = 'other'),
#
# ]

from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
