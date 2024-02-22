from django.contrib import admin
from sugar.models import Food, Country
# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    search_fields = ['origin']


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Food, FoodAdmin)
admin.site.register(Country, CountryAdmin)
