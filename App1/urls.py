from django.urls import path
from App1.views import *
app_name='sai'
urlpatterns=[
    path('data_render/',data_render,name='data_render'),
]