from django.urls import path
from . import views

urlpatterns = [

     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
     path('shows/', views.shows_index, name='index'),
     path('shows/<int:show_id>/', views.shows.detail, name='detail'),
     path('accounts.signup/', views.signup, name='signup')
]

