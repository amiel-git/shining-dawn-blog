from django.db import models
from django.contrib.auth.models import User

## BASE USER ##

class UserProfile(User):
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StaffProfile(User):
    USERNAME_FIELD = 'email'
    is_staff = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
