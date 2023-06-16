from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('shows/', views.shows_index, name='index')
]