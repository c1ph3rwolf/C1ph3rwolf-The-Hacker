from django.urls import path
from . import views

urlpatterns = [
    path('', views.thehome, name='thehome')
]