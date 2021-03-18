from django.contrib import admin

from apps.redirect.models import Redirect


@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    search_fields = ['id', 'key', 'url']
    list_display = ('id', 'key', 'url',)
