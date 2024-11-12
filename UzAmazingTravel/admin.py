from django.contrib import admin

from .models import Contact, Provinces, Carusel


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(Provinces)
class ProvincesAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Carusel)
class CaruselAdmin(admin.ModelAdmin):
    list_display = ['provinces']
