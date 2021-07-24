from django.shortcuts import render

# Create your views here.
def myfridge(request):
    return render(request, 'myfridge.html')

def showdish(request):
    return render(request, 'showdish.html')