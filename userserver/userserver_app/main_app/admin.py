from django.contrib import admin
from .models import ContVote


@admin.register(ContVote)
class ContVote(admin.ModelAdmin):
    list_display = ('vote',)
