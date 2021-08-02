from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from community.models import Post
from django.core.paginator import Paginator

# Create your views here.
def likelist(request):
    posts = Post.objects.all()
    page = request.GET.get('page','1')
    paginator = Paginator(posts, 5)
    page_obj = paginator.page(page)
    return render(request, 'likelist.html', {'posts': page_obj})