from fridge.models import Dish
from community.models import Post
from expert.models import Expert
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.views.decorators.http import require_GET

def myfridge(request):
    return render(request, 'myfridge.html')

@require_GET
def showdish(request):
    allingre = ['밥', '식빵', '달걀', '김치', '햄', '라면', '소면', '파스타면', '칼국수 면', '두부면',
        '닭고기', '닭가슴살', '돼지고기', '삼겹살', '돼지목살', '소고기', '차돌박이',
        '버섯', '파', '양파', '샐러드야채', '시금치', '숙주나물', '콩나물', '당근', '애호박', '고추', '깻잎', '청경채',
        '고추장', '고춧가루', '우유', '잼', '토마토소스', '까르보나라소스', '생크림', '굴소스', '치킨스톡', '통마늘', '다진마늘', '맛술', '불닭소스', '마요네즈', '케찹', '버터',
        '블루베리', '딸기', '바나나', '귤', '사과', '딸기청', '자몽청', '플레인요거트', '그릭요거트', '그래놀라', '시리얼'
        ]
    selected = request.GET.getlist('ingredients', None)
    searched = request.GET.getlist('direct', None)

    if selected :
        if searched[0] != '':  #검색어를 입력하면 selected 리스트에 붙이기
            selected.extend(searched)
        #검색어를 입력하지 않으면 그냥 그대로 진행
        maindish = Dish.objects.all()
        adddish = Dish.objects.all()
        for i in selected:
            if i==selected[0]:
                qm = Q(ingredients__icontains=i)
                q = Q(ingredients__icontains=i)
            else:
                qm &= Q(ingredients__icontains=i) #선택된 재료 모두를 포함하는 요리들
                q |= Q(ingredients__icontains=i)    #선택된 재료 중 하나라도 포함하는 요리들

            for ingre in allingre:
                if i == ingre:
                    allingre.remove(ingre) # 선택하지 않은 재료 = 전체 재료 - 선택한 재료  

        for j in allingre:  # 선택하지 않은 재료를 포함하는 요리 제외
            if j == allingre[0]:
                qe = ~Q(ingredients__icontains = j) 
            else:
                qe &= ~Q(ingredients__icontains=j)
        
        maindish = maindish.filter(qe&qm).order_by('ingredients') 
        adddish = adddish.filter(q).order_by('ingredients')
        return render(request, 'showdish.html', {'maindish': maindish, 'adddish' : adddish, 'selected':selected })
    else:
        if searched[0] != '':  #검색어를 입력하면 selected 리스트에 붙이기
            selected.extend(searched)
            maindish = Dish.objects.all()
            adddish = Dish.objects.all()
            for i in selected:
                if i==selected[0]:
                    qm = Q(ingredients__icontains=i)
                    q = Q(ingredients__icontains=i)
                else:
                    qm &= Q(ingredients__icontains=i) #선택된 재료 모두를 포함하는 요리들
                    q |= Q(ingredients__icontains=i)    #선택된 재료 중 하나라도 포함하는 요리들

                for ingre in allingre:
                    if i == ingre:
                        allingre.remove(ingre) # 선택하지 않은 재료 = 전체 재료 - 선택한 재료  

            for j in allingre:  # 선택하지 않은 재료를 포함하는 요리 제외
                if j == allingre[0]:
                    qe = ~Q(ingredients__icontains = j) 
                else:
                    qe &= ~Q(ingredients__icontains=j)

            maindish = maindish.filter(qe&qm).order_by('ingredients') 
            adddish = adddish.filter(q).order_by('ingredients.count')
            return render(request, 'showdish.html', {'maindish': maindish, 'adddish' : adddish, 'selected':selected })
        else:
            return redirect('myfridge')

def recipy(request, dish_id):
    dish_recipy = get_object_or_404(Dish, pk = dish_id)
    post_object = Post.objects.all()
    expert_object = Expert.objects.all()

    if dish_recipy:
        result = post_object.filter (title__contains=dish_recipy) | post_object.filter(content__contains = dish_recipy)
        result2 = expert_object.filter (title__contains = dish_recipy) | expert_object.filter(body__contains = dish_recipy)
    return render(request, 'recipy.html', {'dish' : dish_recipy, 'result': result, 'result2':result2})
