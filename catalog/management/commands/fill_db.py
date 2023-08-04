from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        products = [
            {'title': 'Клей для обоев', 'description': 'Клей для обоев на площадь 25м2',
             'category': Category.objects.all()[2], 'price': 300},
            {'title': 'Плиточный клей', 'description': 'Плиточный клей для наружных и внутренних работ',
             'category': Category.objects.all()[2], 'price': 500},
            {'title': 'Жидкость для мытья полов', 'description': 'Жидкость для мытья полов с запахом ванили',
             'category': Category.objects.all()[3], 'price': 125},
            {'title': 'Комплект тряпок', 'description': 'Комплект безворсовых тряпок для влажной уборки',
             'category': Category.objects.all()[3], 'price': 70}
        ]

        products_for_create = [Product(**product) for product in products]
        Product.objects.bulk_create(products_for_create)
