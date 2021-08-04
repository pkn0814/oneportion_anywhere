from accounts.models import CustomerUser
import expert
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from . models import Expert, Scrap
from . forms import ExpertForm
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
def expert_list(request):
    experts = Expert.objects.all
    page_list = Expert.objects.order_by('-pub_date')
    paginator = Paginator(page_list, 6)
    
    page = request.GET.get('page','1')
    
    page_obj = paginator.get_page(page)
    

    return render(request, 'expert_list.html',{'experts':experts,'page_list':page_obj})

def detail(request, expert_id):
    expert_detail = get_object_or_404(Expert, pk=expert_id)
    try:
        scrap = Scrap.objects.filter(user=request.user, expert=expert_detail)
        return render(request, 'detail.html', {'expert':expert_detail,'scrap':scrap})
    except:
        return render(request, 'detail.html', {'expert':expert_detail})


    


def new(request):
    return render(request, 'new.html')

def expertcreate(request):
    
    if request.method == 'POST':
        form = ExpertForm(request.POST,request.FILES)
        if form.is_valid():
            
            expert = form.save(commit=True)
            expert.writer = request.user
            expert.save()
            return redirect('expert_list')
        else:
            form = ExpertForm()
            messages.info(request,'본문 내용을 작성해주세요')
            return render(request, 'new.html', {'form':form}) 

    else:
        form = ExpertForm()
        messages.info(request,'작성법 소개')
        return render(request, 'new.html', {'form':form})         



def edit(request):
    return render(request, 'edit.html')

def expertupdate(request, expert_id):
    expert = get_object_or_404(Expert, pk=expert_id)
    
        
    if request.method == 'POST':
        form = ExpertForm(request.POST, instance=expert)
        if form.is_valid():
            expert = form.save(commit=False)
            expert.writer = request.user
            expert.save()
            return redirect('detail',expert_id=expert.pk)
    else:
        form = ExpertForm(instance=expert)
        return render(request, 'edit.html', {'form':form})

def expertdelete(request, expert_id):
    expert = get_object_or_404(Expert, pk=expert_id)
    expert.delete()
    return redirect('expert_list')

def scrap(request, expert_id):
    expert = get_object_or_404(Expert, pk=expert_id)
    scrapped = Scrap.objects.filter(user=request.user, expert=expert)
    if not scrapped:
        Scrap.objects.create(user=request.user, expert=expert)
    else:
        scrapped.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))





