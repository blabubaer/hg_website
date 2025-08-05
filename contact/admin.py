from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'email', 
        'subject', 
        'company', 
        'created_at', 
        'is_read', 
        'is_responded'
    ]
    list_filter = ['is_read', 'is_responded', 'created_at']
    list_editable = ['is_read', 'is_responded']
    search_fields = ['name', 'email', 'subject', 'message', 'company']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Kontaktdaten', {
            'fields': ('name', 'email', 'phone', 'company')
        }),
        ('Nachricht', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'is_responded', 'created_at')
        }),
    )
    
    actions = ['mark_as_read', 'mark_as_responded']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Als gelesen markieren"
    
    def mark_as_responded(self, request, queryset):
        queryset.update(is_responded=True)
    mark_as_responded.short_description = "Als beantwortet markieren"
