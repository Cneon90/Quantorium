from django.contrib import admin
from .models import Profile

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'Phone', 'Status')

admin.site.register(Profile, PostAdmin)