from fridge.models import Dish
from django.shortcuts import redirect, render
from django.db.models import Q 

# Create your views here.
def myfridge(request):
    return render(request, 'myfridge.html')

def showdish(request):
    maindish = Dish.objects.all()
    adddish = Dish.objects.all()
    selectedMain = request.GET.getlist('ingredients')
    selectedAdd = request.GET.getlist('additional')

    if selectedMain:
        for i in selectedMain:
            maindish = maindish.filter(main__icontains=i)
            for k in selectedAdd:
                maindish = maindish.filter(add__icontains=k)
    
    if selectedAdd:
        for k in selectedAdd:
            adddish = adddish.filter(add__icontains=k)
    
    return render(request, 'showdish.html', {'maindish': maindish, 'adddish' : adddish, 'selectedMain':selectedMain, 'selectedAdd' : selectedAdd})
    
