from django.contrib import admin

# Register your models here.

from .models import task, Review

admin.site.register(task)
admin.site.register(Review)
