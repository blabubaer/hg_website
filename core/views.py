from django.shortcuts import render
from projects.models import Project


def home(request):
    """Home page view"""
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    recent_projects = Project.objects.all()[:6]
    
    context = {
        'featured_projects': featured_projects,
        'recent_projects': recent_projects,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page view"""
    return render(request, 'core/about.html')


def services(request):
    """Services page view"""
    return render(request, 'core/services.html')
