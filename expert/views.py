import expert
from django.shortcuts import render, get_object_or_404, redirect
from . models import Expert, Photo
from . forms import ExpertForm
# Create your views here.
def expert_list(request):
    experts = Expert.objects
    return render(request, 'expert_list.html',{'experts':experts})

def detail(request, expert_id):
    expert_detail = get_object_or_404(Expert, pk=expert_id)
    return render(request, 'detail.html', {'expert':expert_detail})


def new(request):
    return render(request, 'new.html')

def expertcreate(request):
    if request.method == 'POST':
        form = ExpertForm(request.POST)
        if form.is_valid():
            expert = form.save(commit=True)
            expert.save()
            return redirect('expert_list')
    else:
        form = ExpertForm()
        return render(request, 'new.html', {'form':form})

def edit(request):
    return render(request, 'edit.html')

def expertupdate(request, expert_id):
    expert = get_object_or_404(Expert, pk=expert_id)
    if request.method == 'POST':
        form = ExpertForm(request.POST, instance=expert)
        if form.is_valid():
            expert = form.save(commit=False)
            expert.save()
            return redirect('detail',expert_id=expert.pk)
    else:
        form = ExpertForm(instance=expert)
        return render(request, 'edit.html', {'form':form})

def expertdelete(request, expert_id):
    expert = get_object_or_404(Expert, pk=expert_id)
    expert.delete()
    return redirect('expert_list')





