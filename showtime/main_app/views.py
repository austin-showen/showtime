from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Show
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render(request, "home.html")
@login_required
def shows_index(request):
    shows = Show.objects.all()
    return render(request, 'shows/index.html', {
        'shows' : shows
    })
@login_required
def shows_detail(request, show_id):
    show = Show.objects.get(id=show_id)
    return render(request, "shows/details.html", {"shows": show})


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

class ShowCreate(LoginRequiredMixin, CreateView):
    model = Show
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class ShowUpdate(LoginRequiredMixin, UpdateView):
    model = Show
    fields = ['date', 'review', 'theater']
class ShowDelete(LoginRequiredMixin, DeleteView):
    model = Show
    success_url = '/shows'
