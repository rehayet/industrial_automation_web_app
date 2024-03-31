from django.urls import path
from . import views
urlpatterns = [

    path('' , views.block , name="block"),
    path('re/' , views.re, name = 're'),



    
]

# Developed by Rehayet Hossen Shakil 
#     https://www.linkedin.com/in/rehayet-hossen-shakil