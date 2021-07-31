from fridge.models import Dish
from django.shortcuts import redirect, render


# Create your views here.
def myfridge(request):
    return render(request, 'myfridge.html')

def showdish(request):
    selectedMain = request.GET.getlist('ingredients')
    selectedAdd = request.GET.getlist('additional')
    ingre = " ".join(selectedMain)
    add = " ".join(selectedAdd)
    dish_obj = Dish.objects
    return render(request, 'showdish.html', {'dishs': dish_obj, 'selectedMain':selectedMain, 'selectedAdd' : selectedAdd})
    
