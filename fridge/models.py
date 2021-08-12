from django.db import models
from cloudinary.models import CloudinaryField


class Dish(models.Model):
    name = models.CharField(max_length=15, default='') #음식 이름
    intro = models.TextField(max_length=30, default='') #음식 간단 소개
    image = CloudinaryField('images/',default='loaddish.jpg',blank=True,null=False)
    basic = models.TextField(max_length=200, default='', blank = True, null=True) #기본재료 중에서 필요한 것
    ingredients = models.TextField(max_length=300, default='') #필요한 재료
    option = models.CharField(max_length=100, default='', blank = True, null = True) #옵션
    recipy = models.TextField(default='', blank=True, null = True)  #레시피

    def __str__(self):
        return self.name 
