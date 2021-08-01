from django.db import models
from accounts.models import CustomerUser

# Create your models here.

class Post(models.Model):
    writer = models.ForeignKey(CustomerUser, related_name="community", on_delete=models.CASCADE, verbose_name="작성자", null=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    

    def __str__(self):
        return self.title