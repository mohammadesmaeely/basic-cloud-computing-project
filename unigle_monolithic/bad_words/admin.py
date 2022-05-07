from django.contrib import admin

from bad_words.models import BadWord


@admin.register(BadWord)
class BadWordAdmin(admin.ModelAdmin):
    model = BadWord
    list_display = ['id', 'word']
