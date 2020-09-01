from django.urls import path

from . import views

#creating an array because we will house multiple URL patterns to be called on. 
#we will assign a path and then the name so views is the file, index is the function
urlpatterns = [
    path('', views.index, name='index'),
]