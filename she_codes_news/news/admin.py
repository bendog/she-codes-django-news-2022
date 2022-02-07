from django.contrib import admin

# Register your models here.
from.models import NewsStory

admin.site.register(NewsStory)
# django then knows this is admin user