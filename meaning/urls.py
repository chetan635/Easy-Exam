from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="MainHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.Contact,name="ContactUs"),
    path("notes/",views.notes,name="notes"),
    path("trans/",views.trans,name="Search"),
    path("pro/",views.pro,name="pro"),
    path("result/",views.result,name="result"),
  
    
]
