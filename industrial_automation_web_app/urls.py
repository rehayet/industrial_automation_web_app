from django.urls import path
from . import views
urlpatterns = [

    path('' , views.block , name="block"),
    path('re/' , views.re, name = 're'),



    
]