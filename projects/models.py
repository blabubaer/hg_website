from django.db import models
from django.utils import timezone


class ProjectCategory(models.Model):
    """Category for organizing projects"""
    name = models.CharField(max_length=100, verbose_name="Kategorie Name")
    description = models.TextField(blank=True, verbose_name="Beschreibung")
    order = models.IntegerField(default=0, verbose_name="Reihenfolge")
    
    class Meta:
        verbose_name = "Projektkategorie"
        verbose_name_plural = "Projektkategorien"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Project(models.Model):
    """Model for storing project/reference information"""
    title = models.CharField(max_length=200, verbose_name="Projekttitel")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-Slug")
    category = models.ForeignKey(
        ProjectCategory, 
        on_delete=models.CASCADE, 
        related_name='projects',
        verbose_name="Kategorie"
    )
    description = models.TextField(verbose_name="Beschreibung")
    short_description = models.CharField(
        max_length=300, 
        blank=True, 
        verbose_name="Kurzbeschreibung"
    )
    client = models.CharField(max_length=200, blank=True, verbose_name="Kunde")
    location = models.CharField(max_length=200, blank=True, verbose_name="Standort")
    completion_date = models.DateField(
        blank=True, 
        null=True, 
        verbose_name="Fertigstellungsdatum"
    )
    main_image = models.ImageField(
        upload_to='projects/main/', 
        verbose_name="Hauptbild"
    )
    is_featured = models.BooleanField(
        default=False, 
        verbose_name="Hervorgehoben"
    )
    order = models.IntegerField(default=0, verbose_name="Reihenfolge")
    created_at = models.DateTimeField(
        default=timezone.now, 
        verbose_name="Erstellt am"
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Aktualisiert am"
    )
    
    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekte"
        ordering = ['-is_featured', 'order', '-completion_date', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('projects:project_detail', kwargs={'slug': self.slug})


class ProjectImage(models.Model):
    """Additional images for projects"""
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='images',
        verbose_name="Projekt"
    )
    image = models.ImageField(
        upload_to='projects/gallery/', 
        verbose_name="Bild"
    )
    caption = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name="Bildunterschrift"
    )
    order = models.IntegerField(default=0, verbose_name="Reihenfolge")
    
    class Meta:
        verbose_name = "Projektbild"
        verbose_name_plural = "Projektbilder"
        ordering = ['order']
    
    def __str__(self):
        return f"{self.project.title} - {self.caption or 'Bild'}"
