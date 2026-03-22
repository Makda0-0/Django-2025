from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Club pages
    path('', views.lobby, name='lobby'),
    path('lounge/', views.member_lounge, name='lounge'),
    path('office/', views.manager_office, name='office'),
]