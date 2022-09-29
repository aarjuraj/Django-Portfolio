from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('programmingprofile', views.programmingprofile, name="programmingprofile"),
    path('webdevelopment', views.webdevelopment, name="webdevelopment"),

]
