from django.db import models

#메인재료
#부가재료
#옵션
#선택요리
#포함요리

MAIN_INGRE = (
         ('밥', '밥'), ('식빵', '식빵'), ('달걀', '달걀'), ('김치', '김치'), ('햄', '햄'), 
        ('라면', '라면'), ('소면', '소면'), ('파스타면', '파스타면'),
        ('닭고기', '닭고기'), ('돼지고기', '돼지고기'), ('소고기', '소고기'), 
        ('버섯', '버섯'), ('파', '파') 
    )

class Ingredients(models.Model):
    main_ingre = models.BooleanField(default=False, choices=MAIN_INGRE)

    def __str__(self):
        return self.main_ingre

class Dish(models.Model):
    name = models.CharField(max_length=15) #음식 이름
    intro = models.CharField(max_length=30) #음식 간단 소개
    picture = models.ImageField #음식 사진
    main = models.CharField #메인재료
    add = models.CharField #부가재료
    option = models.CharField #옵션




