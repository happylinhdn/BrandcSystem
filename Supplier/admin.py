from django.contrib import admin
from .models import Supplier

# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'channel', 'follower', 'kol_tier', 'engagement_rate_absolute_display', 'engagement_rate_percent']
    list_filter = ['gender', 'channel']
    search_fields = ['name']

# Register your models here.
admin.site.register(Supplier, SupplierAdmin)