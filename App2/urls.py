from django.urls import path
from App2.views import *
urlpatterns=[
    path('data_render/',data_render,name='data_render'),
]