from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Theater(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    maps_url = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Show(models.Model):
    name = models.CharField(max_length=100)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    date = models.DateField('Show Date')
    seen = models.ManyToManyField(User, related_name='seen')
    wishlist = models.ManyToManyField(User, related_name='wishlist')
    playbill_url = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.id})"

    def get_absolute_url(self):
        return reverse('shows_index')

    class Meta:
        ordering = ["name"]


class Photo(models.Model):
    url = models.CharField(max_length=200)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for show_id: {self.show_id} @{self.url}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'show_id': self.id})


class Review(models.Model):
    date = models.DateField('Review Date')
    description = models.TextField(max_length=250)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.show} on {self.date}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'show_id':self.show_id})