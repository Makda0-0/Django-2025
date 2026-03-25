from django.contrib import admin
from django.urls import path, include
from club import views as club_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', club_views.home, name='home'),                    # Public lobby
    path('login/', club_views.login_view, name='login'),     
    path('logout/', club_views.logout_view, name='logout'),
    path('lounge/', club_views.member_lounge, name='member_lounge'),
    path('office/', club_views.manager_office, name='manager_office'),
]