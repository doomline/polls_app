"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

#These are the URLs and URL configs. so if you go to localhost 8000/polls it brings up that section
urlpatterns = [

#path() can take 4 arguments. 2 required, 2 not required. 
#1 argument required is route: a string that contains a URL pattern. Patterns don't search GET and POST Params. They just pull info
#2 argument is view: When Django finds a matching pattern, it calls the specified view function with an HTTPRequest object as the first argument and any captured values from the route as keyword arguments.
#3 argument is kwargs(Key Word Arguments(optional)): keyword arguments that can be passed in a dictionary to the target view
#4 argument is name: This gives the URL a name, allowing you to refer to it elsewhere in Django. This means you can make global changes to patterns in just one file
    path('polls/', include('polls.urls')), #include is a plug and play way to pull the URLS. 
    path('admin/', admin.site.urls), 
]
