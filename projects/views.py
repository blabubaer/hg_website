from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Project, ProjectCategory


def project_list(request):
    """List all projects with optional category filtering"""
    category_slug = request.GET.get('category')
    
    if category_slug:
        category = get_object_or_404(ProjectCategory, slug=category_slug)
        projects = Project.objects.filter(category=category)
    else:
        category = None
        projects = Project.objects.all()
    
    # Pagination
    paginator = Paginator(projects, 9)  # 9 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get all categories for filter
    categories = ProjectCategory.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'projects/project_list.html', context)


def project_detail(request, slug):
    """Detail view for a single project"""
    project = get_object_or_404(Project, slug=slug)
    
    # Get related projects (same category, excluding current)
    related_projects = Project.objects.filter(
        category=project.category
    ).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'projects/project_detail.html', context)
