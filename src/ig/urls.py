from django.urls import path
from . import views

appname = "ig"

urlpatterns = [
    path('', views.index, name='index'),
]
