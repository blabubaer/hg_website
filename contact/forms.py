from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Contact form for the website"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'company', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ihr Name *'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ihre E-Mail-Adresse *'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ihre Telefonnummer (optional)'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ihre Firma (optional)'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Betreff *'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Ihre Nachricht *'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make required fields more obvious
        for field_name, field in self.fields.items():
            if field_name in ['name', 'email', 'subject', 'message']:
                field.required = True
                field.widget.attrs['required'] = 'required' 