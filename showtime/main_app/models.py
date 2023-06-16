from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Show(models.Model):
    name = models.CharField(max_length=100)
    theater = models.CharField(max_length=100)
    date = models.DateField('Show Date')
    review = models.TextField(max_length=250)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'show_id': self.id})
