from django.urls import path
from . import views

urlpatterns = [
    path('expert_list/', views.expert_list, name='expert_list' ),
    path('detail/<int:expert_id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('expertcreate/', views.expertcreate, name='expertcreate'),
    path('edit/',views.edit, name='edit'),
    path('expertupdate/<int:expert_id>',views.expertupdate, name='expertupdate'),
    path('expertdelete/<int:expert_id>', views.expertdelete, name='expertdelete'),
    path('scrap/<int:expert_id>', views.scrap, name='scrap'),
    
]