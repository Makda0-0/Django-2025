from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom User Model - ready for future extensions"""
    # Add any additional fields here if needed in the future
    pass
    
    def __str__(self):
        return self.username