from django.contrib import admin

from . import models

class StatusItemInline(admin.TabularInline):
    model = models.Status
    extra = 1

@admin.register(models.Installation)
class InstallationAdmin(admin.ModelAdmin):
    
    inlines = [StatusItemInline]
    list_display = ['customer_name', 'address',
                     'appointment_date']
    # list_filter = ['status']
    list_per_page = 10
    
    # list_prefetch_related = ['status']
    search_fields = ['customer_name__istartswith', 'address']
    ordering = ['-date_modified']

