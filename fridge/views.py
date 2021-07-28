from fridge.models import Ingredients
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import IngreForm

# Create your views here.
def myfridge(request):
    if request.POST:
        ingreform = IngreForm(request.POST)
        if ingreform.is_valid():
            selectedMain = request.POST.getlist('ingredients[]')
            selectedMain = ingreform.save(commit=False)
            selectedMain.save()
            return redirect('showdish')
        else:
            return redirect('showdish')
    else:
        ingreform = IngreForm()
        return render(request, 'myfridge.html', {'ingreform': ingreform })

def showdish(request):
    ingredients = Ingredients.objects.all()
    return render(request, 'showdish.html', {'ingredients': ingredients})
    
