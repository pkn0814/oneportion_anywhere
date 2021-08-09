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
    paginator = Paginator(page_list, 3)
    
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
        message = "밀키트 글을 작성할 경우 본문에 음식 사진과 구매를 위한 사이트 주소를 필수적으로 입력해야 합니다."
        message2 = "파일 선택을 통해 업로드되는 사진은 게시판 글 목록에 대표적으로 표시되는 사진입니다. 본문에 들어갈 사진은 글 작성 에디터에 있는 사진 등록 버튼을 이용해주세요."
        messages.info(request,message)
        messages.info(request, message2)
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





