from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfridge, name='myfridge'),
    path('showdish/', views.showdish, name='showdish'),
]