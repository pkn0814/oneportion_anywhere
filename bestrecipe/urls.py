from django.urls import path
from . import views

urlpatterns = [
    path('likelist/', views.likelist, name='likelist'),
]