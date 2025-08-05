from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm
from .models import ContactMessage


def contact(request):
    """Contact form view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact_message = form.save()
            
            # Send email notification
            try:
                send_contact_email(contact_message)
                messages.success(
                    request, 
                    'Vielen Dank für Ihre Nachricht! Wir werden uns schnellstmöglich bei Ihnen melden.'
                )
            except Exception as e:
                # Log the error but don't show it to the user
                print(f"Email sending failed: {e}")
                messages.success(
                    request, 
                    'Vielen Dank für Ihre Nachricht! Wir werden uns schnellstmöglich bei Ihnen melden.'
                )
            
            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})


def send_contact_email(contact_message):
    """Send email notification for new contact message"""
    subject = f"Neue Kontaktanfrage: {contact_message.subject}"
    
    # Email content
    context = {
        'contact_message': contact_message,
    }
    
    html_message = render_to_string('contact/email/contact_notification.html', context)
    plain_message = render_to_string('contact/email/contact_notification.txt', context)
    
    # Send email to business
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],  # Send to business email
        html_message=html_message,
        fail_silently=False,
    )
