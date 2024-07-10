from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Profile(AbstractUser):
    phone_number = models.CharField(max_length=120, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)


    groups = models.ManyToManyField(Group,
                                    blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True,
                                              related_name='custom_user_permissions')

