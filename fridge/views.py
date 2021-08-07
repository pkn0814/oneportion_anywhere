from fridge.models import Dish
from django.shortcuts import redirect, render
from django.db.models import Q

def myfridge(request):
    return render(request, 'myfridge.html')


def showdish(request):
    allingre = ['밥', '식빵', '달걀', '김치', '햄', '라면', '소면', '파스타면', '두부면',
        '닭고기', '닭가슴살', '돼지고기', '삼겹살', '돼지목살', '소고기', '차돌박이',
        '버섯', '파', '양파', '샐러드야채', '시금치', '숙주나물', '콩나물',
        '고추장', '고춧가루', '우유', '잼', '토마토소스', '까르보나라소스', '간장', '생크림', '굴소스', '치킨스톡', '통마늘', '다진마늘', '맛술', '불닭소스',
        '딸기청', '자몽청', '플레인요거트'
        ]
    selected = request.GET.getlist('ingredients', None)

    if selected :
        maindish = Dish.objects.all()
        for i in selected:

            if i==selected[0]:
                qm = Q(ingredients__icontains=i)
                q = Q(ingredients__icontains=i)
            else:
                qm &= Q(ingredients__icontains=i) #선택된 재료 모두를 포함하는 요리들
                q |= Q(ingredients__icontains=i)

            for ingre in allingre:
                if i == ingre:
                    allingre.remove(ingre) # 선택하지 않은 재료 = 전체 재료 - 선택한 재료  

        for j in allingre:  # 선택하지 않은 재료를 포함하는 요리 제외
            if j == allingre[0]:
                qe = ~Q(ingredients__icontains = j) 
            else:
                qe &= ~Q(ingredients__icontains=j)

        maindish = maindish.filter(qe&qm).order_by('ingredients') 
        adddish = Dish.objects.filter(q).order_by('ingredients')

        return render(request, 'showdish.html', {'maindish': maindish, 'adddish' : adddish, 'selected':selected })
    else:
        return redirect('myfridge')
