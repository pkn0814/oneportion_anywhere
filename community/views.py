from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import PostForm
from .models import Post, Scrap_commu
from django.contrib import messages
from django.core.paginator import Paginator

def list(request):
    posts = Post.objects.all()
    page = request.GET.get('page','1')
    paginator = Paginator(posts, 5)
    page_obj = paginator.page(page)
    return render(request, 'list.html', {'posts': page_obj})

def postshow(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'postshow.html', {'post': post})

def postnew(request):
    if request.user.is_authenticated: 
        return render(request, 'postnew.html')

def postcreate(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=True)
            post.writer = request.user
            post.save()
            return redirect('list')
    else:
        form = PostForm()
        return render(request, 'postnew.html', {'form':form})  

def edit(request):
    return render(request, 'edit.html')

def postupdate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('postshow', post_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form':form})

def postdelete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('list')

def communityscrap(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    scrapped = Scrap_commu.objects.filter(user=request.user, post=post)
    if not scrapped:
        Scrap_commu.objects.create(user=request.user, post=post)
    else:
        scrapped.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def likes(request, post_id): 
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.writer:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        post.like.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    #return redirect('list')