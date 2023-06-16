from django.shortcuts import render


def home(request):
  return render(request, 'home.html')

def shows_index(request):
    return render(request, 'shows/index.html', {
        'shows' : shows
    })