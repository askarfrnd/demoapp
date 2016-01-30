from django.contrib import admin

from .models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'timestamp_created')

admin.site.register(Log, LogAdmin)