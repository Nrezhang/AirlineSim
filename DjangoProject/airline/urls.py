from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('', views.index, name='v1'),
    #login/logout
    path('Userlogin/', views.userlogin, name='userlogin'),
    path('Agentlogin/', views.agentlogin, name='agentlogin'),
    path('Stafflogin/', views.stafflogin, name='stafflogin'),

    
    ]