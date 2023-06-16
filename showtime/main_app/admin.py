from django.contrib import admin
from .models import Show, Theater, Photo, Review

# Register your models here.
admin.site.register(Show)
admin.site.register(Theater)
admin.site.register(Photo)
admin.site.register(Review)
