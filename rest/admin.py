from django.contrib import admin

# Register your models here.
from rest.models import Dog, Activity, Profile

admin.site.register(Dog)
admin.site.register(Activity)
admin.site.register(Profile)
