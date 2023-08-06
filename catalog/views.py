from django.shortcuts import render
from catalog.models import Product, Contacts


def index(request):
    # Вывод  в консоль последних пяти добавленных товаров
    lst = Product.objects.all().order_by('pk').reverse()[:5]
    print(*lst, sep='\n')
    context = {
        'items': Product.objects.all()
    }

    return render(request, 'catalog/index.html', context)


def contacts(request):
    company_contacts = Contacts.objects.all()
    context = {
        'contacts': company_contacts[0]
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html', context)


def item_info(request, pk):
    context = {
        'item': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/item_info.html', context)
