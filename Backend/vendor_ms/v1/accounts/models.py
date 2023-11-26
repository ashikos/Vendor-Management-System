from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser ,Group, Permission
from v1.accounts.constants import GenderTypes

# Create your models here.


class ProjectUser(AbstractUser): 

    dob = models.DateField(null=True, blank=True)
    gender = models.IntegerField(
        default=GenderTypes.Male, choices=GenderTypes.choices())
    blocked = models.BooleanField(default=False)
 
