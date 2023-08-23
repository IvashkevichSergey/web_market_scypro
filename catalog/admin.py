from django.contrib import admin

from catalog.models import Category, Product, Contacts, Blog, Version


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


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'created_at', 'is_published')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Version)
class AdminVersion(admin.ModelAdmin):
    list_display = ('pk', 'product', 'version_number', 'version_name', 'is_current')