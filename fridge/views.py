from fridge.models import Ingredients, Dish
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import IngreForm

# Create your views here.
def myfridge(request):
    if request.POST:
        ingreform = IngreForm(request.POST)
        if ingreform.is_valid():
            selectedMain = ingreform.save(commit=False)
            selectedMain.save()
            selectedMain = request.POST.getlist('ingredients[]')
            ingre = " ".join(selectedMain)
            dish_obj = Dish.objects.filter(main=ingre)
            return render(request, 'showdish.html', {'dishes': dish_obj, 'selectedMain':selectedMain})
        else:
            return redirect('showdish')
    else:
        ingreform = IngreForm()
        return render(request, 'myfridge.html', {'ingreform': ingreform })

def showdish(request):
    #ingredients = Ingredients.objects.all()
    selectedMain = request.GET.getlist('ingredients')
    selectedAdd = request.GET.getlist('additional[]')
    ingre = " ".join(selectedMain)
    add = " ".join(selectedAdd)
    dish_obj = Dish.objects.filter(main=ingre, add = add)
    return render(request, 'showdish.html', {'dishes': dish_obj, 'selectedMain':selectedMain, 'selectedAdd' : selectedAdd})
    
