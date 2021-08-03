from fridge.models import Dish
from django.shortcuts import get_list_or_404, redirect, render

def myfridge(request):
    return render(request, 'myfridge.html')

def showdish(request):
    maindish = Dish.objects.all()
    adddish = Dish.objects.all()
    selectedMain = request.GET.getlist('ingredients', None)
    selectedAdd = request.GET.getlist('additional', None)
    
    #list = ['올리브유', '우유', '잼', '토마토소스', '간장', '굴소스', '치킨스톡', '고춧가루', '고추장', '설탕', '다진마늘', '양파']
    
    if selectedMain :

        for i in selectedMain:
            maindish = maindish.filter(main__icontains= i)
            adddish = adddish.filter(main__icontains = i)

            if selectedAdd:
                for k in selectedAdd:
                    maindish = maindish.filter(add__icontains = k)
            else :
                adddish = adddish.filter(add__isnull = False) 
            
            maindish = maindish.order_by('main', 'add')
            adddish = adddish.order_by('main', 'add')

    return render(request, 'showdish.html', {'maindish': maindish, 'adddish' : adddish, 'selectedMain':selectedMain, 'selectedAdd' : selectedAdd })
    
