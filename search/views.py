from django.shortcuts import render
from community.models import Post
# Create your views here.

def result(request):
    post_object = Post.objects.all()
    query = request.GET.get('query', '')
    if query:
        result = post_object.filter (title__contains=query) | post_object.filter(content__contains = query)
    return render(request, 'result.html', {'result': result})

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})

def search(request):
    return render(request, 'main.html')