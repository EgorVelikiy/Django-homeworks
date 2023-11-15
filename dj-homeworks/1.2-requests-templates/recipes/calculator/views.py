from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def dish(request):
    servings = int(request.GET.get("servings", 1))
    dish = request.path_info[1:-1]
    context = {'recipe': {}}
    if servings > 1:
        for ingr, amount in DATA[dish].items():
            context['recipe'][ingr] = amount * servings
    else:
        context['recipe'] = DATA[dish]

    return render(request, 'calculator/index.html', context)