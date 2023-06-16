
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from main_app.models import Show


def home(request):
    return render(request, "home.html")

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

def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            error_message = "Invalid signup - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)

