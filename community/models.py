from django.db import models
from accounts.models import CustomerUser

# Create your models here.

class Post(models.Model):
    writer = models.ForeignKey(CustomerUser, related_name="community", on_delete=models.CASCADE, verbose_name="작성자", null=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="글작성일", null=True)
    like = models.ManyToManyField(CustomerUser, related_name='likes', blank=True)
    
    def __str__(self):
        return self.title

class Scrap_commu(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)