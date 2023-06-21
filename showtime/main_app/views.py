import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Show
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from main_app.models import Show, Photo, Theater, Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    theaters = Theater.objects.all()
    shows = Show.objects.all()
    return render(request, 'home.html', {'theaters': theaters, 'shows': shows})


@login_required
def shows_index(request):
    user = request.user
    shows = Show.objects.all()
    seen = user.seen.all()
    wishlist = user.wishlist.all()
    return render(request, 'shows/index.html', {
        'shows': shows,
        'seen': seen,
        'wishlist': wishlist
    })


@login_required
def shows_detail(request, show_id):
    show = Show.objects.get(id=show_id)
    reviews = Review.objects.filter(show=show_id)
    return render(request, "shows/detail.html", {"show": show, "reviews": reviews})



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


def add_photo(request, show_id):
    photo_file = request.FILES.get("photo-file", None)
    if photo_file:
        s3 = boto3.client("s3")
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind(".") :]
        try:
            bucket = os.environ["S3_BUCKET"]
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, show_id=show_id)
        except Exception as e:
            print("An error occurred uploading file to S3")
            print(e)
    return redirect("detail", cat_id=cat_id)


@login_required
def seen_add(request, show_id):
    user = request.user
    show = Show.objects.get(id=show_id)
    user.seen.add(show)
    return redirect('shows_index')


@login_required
def seen_delete(request, show_id):
    user = request.user
    show = Show.objects.get(id=show_id)
    user.seen.remove(show)
    return redirect('shows_index')


@login_required
def wishlist_add(request, show_id):
    user = request.user
    show = Show.objects.get(id=show_id)
    user.wishlist.add(show)
    return redirect('shows_index')


@login_required
def wishlist_delete(request, show_id):
    user = request.user
    show = Show.objects.get(id=show_id)
    user.wishlist.remove(show)
    return redirect('shows_index')

class ShowCreate(LoginRequiredMixin, CreateView):
    model = Show
    fields = ['name', 'date', 'theater']
    success_url = ''

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowUpdate(LoginRequiredMixin, UpdateView):
    model = Show
    fields = ['date', 'review', 'theater']


class ShowDelete(LoginRequiredMixin, DeleteView):
    model = Show
    success_url = '/shows'


@login_required
def theaters_index(request):
    theaters = Theater.objects.all()
    return render(request, 'theaters/index.html', {'theaters': theaters})


@login_required
def theaters_detail(request, theater_id):
    theater = Theater.objects.get(id=theater_id)
    shows = Show.objects.filter(theater=theater_id)
    return render(request, 'theaters/detail.html', {'theater': theater, 'shows': shows})

class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['date', 'description', 'show']

class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = 'shows/<int:show_id>/'

def about(request):
    return render(request, 'about.html')