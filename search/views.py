from django.shortcuts import render
from community.models import Post
from expert.models import Expert
# Create your views here.

def result(request):
    post_object = Post.objects.all()
    expert_object = Expert.objects.all()
    query = request.GET.get('query', '')

    if query:
        result = post_object.filter (title__contains=query) | post_object.filter(content__contains = query) | post_object.filter(tag__contains=query)
        result2 = expert_object.filter (title__contains = query) | expert_object.filter(body__contains = query)
    return render(request, 'result.html', {'result': result, 'result2':result2})

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})

def search(request):
    return render(request, 'main.html')