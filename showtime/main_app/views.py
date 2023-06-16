import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from main_app.models import Show, Photo


def home(request):
    return render(request, "home.html")


def shows_index(request):
    shows = Show.objects.all()
    return render(request, "shows/index.html", {"shows": shows})


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
