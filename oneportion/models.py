from django.db import models
from accounts.models import CustomerUser
# Create your models here.

class Profile(models.Model):
    picture = models.ForeignKey(CustomerUser, related_name="profile", on_delete=models.CASCADE, verbose_name="프사", null=True)

    def __str__(self):
        return self.picture