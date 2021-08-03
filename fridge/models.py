from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=15, default='') #음식 이름
    intro = models.TextField(max_length=30, default='') #음식 간단 소개
    image = models.ImageField(upload_to = 'images/', default='', blank = True, null=True) #음식 사진
    main = models.CharField(max_length=100, default='') #메인재료
    add = models.CharField(max_length=100, default='') #부가재료
    option = models.CharField(max_length=100, default='') #옵션

    def __str__(self):
        return self.name 



