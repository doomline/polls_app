from django.urls import path

from . import views

#creating an array because we will house multiple URL patterns to be called on. 
#we will assign a path and then the name so views is the file, index is the function
#the paths is defined as such, the views index which defaults to the name of the app
# the path set up then defaults to how the views were set up. 
# <int:question_id> stands for integer datatype, then question id. 
# /results/ meaning what the URL. Then the, views.results references that module 
# when someone goes to the site, and they enter in polls/34 it first finds the URLconf mapped to the URLS.
# It finds the polls app, bringing it here. then follows the paths. 

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

