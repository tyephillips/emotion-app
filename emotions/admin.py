from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Emotion, Affirmation

admin.site.register(Emotion)
admin.site.register(Affirmation)
