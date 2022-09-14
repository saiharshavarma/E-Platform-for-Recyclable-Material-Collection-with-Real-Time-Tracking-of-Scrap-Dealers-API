from django.contrib import admin
from .models import Profile, ProfileType

admin.site.register(ProfileType)
admin.site.register(Profile)
