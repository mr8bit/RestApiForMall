from django.contrib import admin
from .models import *





class TerminalAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')


admin.site.register(Terminal, TerminalAdmin)
