from django.http.response import HttpResponseRedirect
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('result', views.process),      # this is "result" path called by Form action setting in index.html on POST request; invokes method .process from views.py
]
