from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('ueber-uns/', views.about, name='about'),
    path('leistungen/', views.services, name='services'),
] 