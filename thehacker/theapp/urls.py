from django.urls import path
from . import views

urlpatterns = [

    path('', views.home_view, name='home'),
    path('base/', views.base_view, name='base'),
    path('browse/', views.browse_view, name='browse'),
    path('details/', views.details_view, name='details'),
    path('profile/', views.profile_view, name='profile'),
    path('tools/', views.tools_view, name='tools'),
    # path('streams/', views.tools_view, name='home')

]