from django.shortcuts import render
from main_app.models import Show

def home(request):
  return render(request, 'home.html')

def shows_index(request):
    shows = Show.objects.all()
    return render(request, 'shows/index.html', {
        'shows' : shows
    })