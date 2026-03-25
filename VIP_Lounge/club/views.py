from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required

# Public home (anyone can see)
def home(request):
    return render(request, 'home.html')

# Simple wrappers for built-in views (you can also use as_view() directly in urls)
def login_view(request):
    return auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True
    )(request)

def logout_view(request):
    return auth_views.LogoutView.as_view(next_page='home')(request)

@login_required(login_url='login')   # Redirects to login if not authenticated
def member_lounge(request):
    return render(request, 'lounge.html')

@login_required(login_url='login')
@permission_required('auth.view_group', raise_exception=True)  # or any permission you assigned
def manager_office(request):
    return render(request, 'office.html')