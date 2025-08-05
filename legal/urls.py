from django.urls import path
from . import views

app_name = 'legal'

urlpatterns = [
    path('datenschutz/', views.privacy_policy, name='privacy_policy'),
    path('cookie-richtlinie/', views.cookie_policy, name='cookie_policy'),
] 