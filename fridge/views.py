from fridge.models import Dish
from django.shortcuts import redirect, render


# Create your views here.
def myfridge(request):
    return render(request, 'myfridge.html')

def showdish(request):
    maindish = Dish.objects.all()
    selectedMain = request.GET.getlist('ingredients')
    if selectedMain:
        for i in selectedMain:
            maindish = maindish.filter(main__icontains=i)
    
    adddish = Dish.objects.all()
    selectedAdd = request.GET.getlist('additional')
    if selectedAdd:
        for k in selectedAdd:
            adddish = adddish.filter(main__icontains=k)
    
    return render(request, 'showdish.html', {'dishs': maindish, 'selectedMain':selectedMain, 'selectedAdd' : selectedAdd})
    
