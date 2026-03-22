from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def lobby(request):
    """Public lobby view - accessible to everyone"""
    return render(request, 'club/lobby.html')

@login_required
def member_lounge(request):
    """Member lounge - only for authenticated users"""
    return render(request, 'club/lounge.html')

def is_manager(user):
    return user.groups.filter(name='Managers').exists() or user.is_superuser

@login_required
@user_passes_test(is_manager)
def manager_office(request):
    """Manager office - only for users in Managers group"""
    return render(request, 'club/office.html')