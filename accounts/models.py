from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from cloudinary.models import CloudinaryField

# Create your models here.

class CustomerUser(AbstractUser):
    POSITION = (
        ('일반', '일반'),
        ('사업자', '사업자'),
    )
    position = models.CharField(verbose_name='등급', max_length=1000, choices=POSITION)
    upload = CloudinaryField('uploads',blank=True,null=True)
    profile = CloudinaryField('images/',default='default_susbwu.JPG',blank=True,null=False)
    nickname = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nickname