from django.db import models
from django.db.models.deletion import PROTECT

class Dish(models.Model):
    name = models.CharField(max_length=15) #음식 이름
    intro = models.TextField(max_length=30) #음식 간단 소개
    image = models.ImageField(upload_to = 'images/') #음식 사진
    main = models.CharField(max_length=100) #메인재료
    add = models.CharField(max_length=100) #부가재료
    option = models.CharField(max_length=100) #옵션

    def __str__(self):
        return self.name 



