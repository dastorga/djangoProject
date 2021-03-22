from django.contrib import admin

from django.contrib import admin
from .models import Redirect

class RedirectAdmin(admin.ModelAdmin):
  list_display = ('id', 'key', 'url', 'active', 'create_at', 'update_at')
  list_display_links = ('id', 'key', 'url')
  search_fields = ('key','active')
  list_per_page = 25

admin.site.register(Redirect, RedirectAdmin)

