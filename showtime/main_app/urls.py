from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shows/", views.shows_index, name="index"),
    path("shows/<int:show_id>/", views.shows_detail, name="detail"),
    path("accounts.signup/", views.signup, name="signup"),
    path("shows/<int:show_id>/add_photo/", views.add_photo, name="add_photo"),
]
