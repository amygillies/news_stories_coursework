from django.contrib import admin

# Register your models here.
from news_stories.models import Story

admin.site.register(Story)