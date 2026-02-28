from django.urls import path, include  # Add 'include' if not already there

urlpatterns = [
    path('api/', include('books.urls')),  # Add this line
    # ... existing paths ...
]
