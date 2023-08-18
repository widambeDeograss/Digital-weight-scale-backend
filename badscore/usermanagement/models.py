from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    ADMIN = 1
    CORPORATE_ADM = 2
    FARMER = 3
    ROLES_CHOICES = (
        (ADMIN, 'system admin'),
        (CORPORATE_ADM, 'corporate admin'),
        (FARMER, 'farmer'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)
    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    last_password_change = models.DateTimeField(null=True)
    role = models.PositiveIntegerField(choices=ROLES_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name', 'phone_number', 'username', 'role']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'
