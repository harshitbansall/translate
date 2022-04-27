from django.contrib import admin

# Register your models here.
from .models import Project, Sentence

admin.site.register(Project)
admin.site.register(Sentence)
