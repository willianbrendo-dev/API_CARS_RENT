from django.contrib import admin
from .models import Car, CarImage, Review


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 3  # Define o número de campos de imagem vazios a serem exibidos


class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price_per_day', 'fuel_type', 'transmission', 'capacity', 'is_favorite')
    list_filter = ('type', 'fuel_type', 'transmission', 'is_favorite')
    search_fields = ('name',)
    ordering = ('name',)
    list_editable = ('is_favorite',)
    inlines = [CarImageInline]


admin.site.register(Car, CarAdmin)
admin.site.register(CarImage)
admin.site.register(Review)
