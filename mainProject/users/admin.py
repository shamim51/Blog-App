from cProfile import Profile
from django.contrib import admin

# Register your models here.
from .models import profile

admin.site.register(profile)
