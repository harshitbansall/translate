from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return '{}'.format(self.full_name)
