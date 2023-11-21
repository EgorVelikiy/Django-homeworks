from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    sort = request.GET.get('sort', None)
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    template = 'catalog.html'
    context = {'phones': phones,
               'sort': sort}
    return render(request, template, context)


def show_product(request, slug):
    phones = Phone.objects.all()
    template = 'product.html'
    for phone in phones:
        if phone['slug'] == slug:
            context = {'phone': phone}
            return render(request, template, context)
