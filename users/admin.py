from django.contrib import admin
from .models import Profile, Gender, Tag

# Register your models here.
admin.site.register(Profile)
admin.site.register(Gender)
admin.site.register(Tag)