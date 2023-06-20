from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('shows/', views.shows_index, name='index'),
     path('shows/<int:show_id>/', views.shows_detail, name='detail'),
     path('shows/create/', views.ShowCreate.as_view(), name='shows_create'),
     path('shows/<int:pk>/update', views.ShowUpdate.as_view(), name='shows_update'),
     path('shows/<int:pk>/delete', views. ShowDelete.as_view(), name='shows_delete'),
     path('shows/seen/', views.seen_index, name='seen_index'),
     path('shows/<int:show_id>/seen/', views.seen_add, name='seen_add'),
     path('shows/wishlist/', views.wishlist_index, name='wishlist_index'),
     path('shows/<int:show_id>/wishlist/', views.wishlist_add, name='wishlist_add'),
     path('accounts.signup/', views.signup, name='signup'),
     path('shows/<int:show_id>/add_photo/', views.add_photo, name='add_photo'),
     path('theaters/', views.theaters_index, name='theaters_index'),
     path('theaters/<int:theater_id>', views.theaters_detail, name='theaters_detail')
]
