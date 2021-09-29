from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Dog(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    birthday = models.DateField()
    anniversary = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/dog-profiles")

    def __str__(self):
        return self.name + " " + self.breed

    def get_absolute_url(self):
        return reverse('dog-detail', args=(str(self.id)))
