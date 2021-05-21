from django.contrib import admin
from .models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','available','created']
    list_editable = ['price','available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

