from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Theater(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
   

    def __str__(self):
        return f"{self.name} ({self.date})"

class Show(models.Model):
    name = models.CharField(max_length=100)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    date = models.DateField('Show Date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
       return reverse('detail', kwargs={'show_id': self.id})

class Review(models.Model):
    date = models.DateField('Review Date')
    description = models.TextField(max_length=250)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_review_display()} on {self.date}"

