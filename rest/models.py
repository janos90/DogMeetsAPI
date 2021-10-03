from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.urls import reverse


class Owner(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
    )
    image = models.ImageField(null=True, blank=True, upload_to="images/owners")
    phone = models.CharField(max_length=20)
    bio = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()


class Dog(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    birthday = models.DateField()
    anniversary = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/dog-profiles")

    def __str__(self):
        return self.name + " the " + self.breed

    def get_absolute_url(self):
        return reverse('dog-detail', args=(str(self.id)))


class Activity(models.Model):
    participants = models.ManyToManyField(Owner)
    dogs = models.ManyToManyField(Dog)
    location = models.CharField(max_length=255)
    startTime = models.DateTimeField()
