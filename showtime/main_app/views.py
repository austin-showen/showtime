from django.shortcuts import render
from main_app.models import Show

def home(request):
  return render(request, 'home.html')

def shows_index(request):
    shows = Show.objects.all()
    return render(request, 'shows/index.html', {
        'shows' : shows
    })

def shows_detail(request, show_id):
    show = Show.objects.get(id=show_id)
    return render(request, 'shows/details.html', {
        'shows': show
    })

# def signup(request):
#     error_message = ''
#     if request.method == 'POST'
#         form = UserCreationForm9request.POST