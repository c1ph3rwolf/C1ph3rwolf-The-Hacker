from django.urls import path 
from . import views

urlpatterns = [
    path('tools/', views.thetools, name='thetools')
]