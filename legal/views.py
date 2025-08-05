from django.shortcuts import render

# Create your views here.

def privacy_policy(request):
    """Privacy policy page view."""
    return render(request, 'legal/privacy_policy.html')

def cookie_policy(request):
    """Cookie policy page view."""
    return render(request, 'legal/cookie_policy.html')
