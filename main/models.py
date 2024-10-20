from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    role = models.IntegerField()
    base_role = 0

    # Add related_name arguments to avoid the clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='main_user_set',  # Add related_name here
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='main_user_permissions_set',  # Add related_name here
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def save(self, *args, **kwargs):
        if not self.pk and self.role is None:
            self.role = self.base_role
        super().save(*args, **kwargs)


class OwnerManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        queryset = super().get_queryset(*args,**kwargs)
        return queryset.filter(role=0)

class Owner(User):
    owners = OwnerManager()
    base_role = 0
    class Meta:
        proxy = True

class CustomerManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        queryset = super().get_queryset(*args,**kwargs)
        return queryset.filter(role=1)

class Customer(User):
    customers = CustomerManager()
    base_role = 1
    class Meta:
        proxy = True

