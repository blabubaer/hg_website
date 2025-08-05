from django.contrib import admin
from django.utils.html import format_html
from .models import Project, ProjectCategory, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ['image', 'caption', 'order']


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'project_count']
    list_editable = ['order']
    search_fields = ['name']
    ordering = ['order', 'name']
    
    def project_count(self, obj):
        return obj.projects.count()
    project_count.short_description = "Anzahl Projekte"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title', 
        'category', 
        'client', 
        'completion_date', 
        'is_featured', 
        'order',
        'image_preview'
    ]
    list_filter = ['category', 'is_featured', 'completion_date', 'created_at']
    list_editable = ['is_featured', 'order']
    search_fields = ['title', 'client', 'description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    inlines = [ProjectImageInline]
    
    fieldsets = (
        ('Grundinformationen', {
            'fields': ('title', 'slug', 'category', 'description', 'short_description')
        }),
        ('Details', {
            'fields': ('client', 'location', 'completion_date')
        }),
        ('Bilder', {
            'fields': ('main_image',)
        }),
        ('Einstellungen', {
            'fields': ('is_featured', 'order')
        }),
    )
    
    def image_preview(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.main_image.url
            )
        return "Kein Bild"
    image_preview.short_description = "Vorschau"
