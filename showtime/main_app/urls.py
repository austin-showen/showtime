from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('shows/', views.shows_index, name='index'),
     path('shows/<int:show_id>/', views.shows_detail, name='detail'),
     path('shows/create/', views.ShowCreate.as_view(), name='shows_create'),
     path('shows/<int:pk>/update', views.ShowUpdate.as_view(), name='shows_update'),
     path('shows/<int:pk>/delete', views. ShowDelete.as_view(), name='shows_delete'),
    #  path('user/<int:user_id>/seen', views.seen, name='seen'),
    #  path('user/<int:user_id>/wishlist', views.wishlist, name='wishlist'),
     path('accounts.signup/', views.signup, name='signup'),
     path('shows/<int:show_id>/add_photo/', views.add_photo, name='add_photo'),
     path('theaters/', views.theaters_index, name='theaters_index'),
]
