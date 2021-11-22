from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
    )
    image = models.ImageField(null=True, blank=True, upload_to="images/owners")
    phone = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)


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
        return self.name + " the " + self.breed

    def get_absolute_url(self):
        return reverse('dog-detail', args=(str(self.id)))


class Activity(models.Model):
    name = models.CharField(max_length=255)

    location = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    startTime = models.DateTimeField()
    description = models.TextField()

    dogs = models.ManyToManyField(Dog, blank=True)
    participants = models.ManyToManyField(User, related_name='activities', blank=True)
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='myActivities',
                              related_query_name="activity"
                              )
