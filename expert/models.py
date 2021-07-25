from django.db import models
from accounts.models import CustomerUser

class Expert(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    user = models.ForeignKey(CustomerUser, related_name="expert_user", on_delete=models.CASCADE,db_column="user")
    body = models.TextField()

    def __str__(self):
        return self.title

class Photo(models.Model):
    expert = models.ForeignKey(Expert, related_name="expert_photo", on_delete=models.CASCADE, db_column="expert_photo" )
    image = models.ImageField(upload_to='images/',blank=True,null=True)

    