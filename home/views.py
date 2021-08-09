from django.shortcuts import render
import random
# Create your views here.

def main(request):
    return render(request, 'main.html')