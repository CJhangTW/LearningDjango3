from django.urls import path
from . import views

app_name = "ig"

urlpatterns = [
    path('', views.index, name='index'),
]
