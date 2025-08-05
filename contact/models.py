from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    """Model for storing contact form submissions"""
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="E-Mail")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    company = models.CharField(max_length=200, blank=True, verbose_name="Firma")
    subject = models.CharField(max_length=200, verbose_name="Betreff")
    message = models.TextField(verbose_name="Nachricht")
    created_at = models.DateTimeField(
        default=timezone.now, 
        verbose_name="Eingegangen am"
    )
    is_read = models.BooleanField(
        default=False, 
        verbose_name="Gelesen"
    )
    is_responded = models.BooleanField(
        default=False, 
        verbose_name="Beantwortet"
    )
    
    class Meta:
        verbose_name = "Kontaktnachricht"
        verbose_name_plural = "Kontaktnachrichten"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%d.%m.%Y')})"
    
    def get_short_message(self):
        """Return first 100 characters of message"""
        return self.message[:100] + "..." if len(self.message) > 100 else self.message
