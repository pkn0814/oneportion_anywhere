from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.views.decorators.http import require_POST
from .forms import IngreForm
from django.contrib import messages

# Create your views here.
def myfridge(request):
    ingreform = IngreForm()
    return render(request, 'myfridge.html', {'ingreform': ingreform })

def showdish(request):
    if request.POST:
        ingreform = IngreForm(request.POST)
        if ingreform.is_valid():
            selectedMain = request.POST.getlist('ingredients[]')
            selectedMain = ingreform.save(commit=False)
            selectedMain.save()
            return render(request, 'showdish.html', {'selectedMain':selectedMain, 'ingreform': ingreform })
        else:
            return redirect('showdish')
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
def dishes(request):
    return render(request, 'dishes.html')
