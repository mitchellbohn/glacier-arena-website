from django.contrib import admin
from .models import *

# Register your models here.

class TeamsInline(admin.TabularInline): 
    model = Team
    extra = 0

class GamesInline(admin.TabularInline):
    model = Game
    extra = 0

class LeagueAdmin(admin.ModelAdmin):
    inlines = [TeamsInline, GamesInline]

admin.site.register(League, LeagueAdmin)

