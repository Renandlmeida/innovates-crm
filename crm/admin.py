from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'status', 'potential_value', 'updated_at')
    list_filter = ('status',)
    search_fields = ('name', 'phone', 'email', 'company')
