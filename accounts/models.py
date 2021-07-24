from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomerUser(AbstractUser):
    POSITION = (
        ('일반', '일반'),
        ('사업자', '사업자'),
    )
    position = models.CharField(verbose_name='등급', max_length=1000, choices=POSITION)
    upload = models.FileField(upload_to='uploads/')
    nickname = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nickname