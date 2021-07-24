from django.shortcuts import render

# Create your views here.
def myfridge(request):
    return render(request, 'myfridge.html')

def selected(request):
    selectedMain = request.POST.getlist('ingredients[]')
    selectedAdd = request.POST.getlist('Additional[]')

def showdish(request):
    return render(request, 'showdish.html')