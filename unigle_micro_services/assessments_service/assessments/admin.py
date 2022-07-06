from django.contrib import admin

from assessments.models import Assessment


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    model = Assessment
    list_display = ['id', 'registrar', 'present']
