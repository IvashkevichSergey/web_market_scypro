from django.contrib import admin

from catalog.models import Category, Product, Contacts


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')
    list_filter = ('category', )
    search_fields = ('title', 'description')


@admin.register(Contacts)
class AdminContacts(admin.ModelAdmin):
    list_display = ('address', 'phone_number')