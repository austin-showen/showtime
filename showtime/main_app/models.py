from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Show(models.Model):
    name = models.CharField(max_length=100)
    theater = models.CharField(max_length=100)
    date = models.DateField("Show Date")
    review = models.TextField(max_length=250)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.id})"

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'show_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for show_id: {self.show_id} @{self.url}"
