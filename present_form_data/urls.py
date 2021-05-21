from django.http.response import HttpResponseRedirect
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('process', views.process),         # this is "process" path called by Form action setting in index.html on POST request
    path('result', views.result),         # this is "result" path to which the .process method will redirect
]
