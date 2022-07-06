from django.contrib import admin
from presents.models import Present, University, Lecture, Teacher


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    model = University
    list_display = ['id', 'name']


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    model = Lecture
    list_display = ['id', 'name']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    list_display = ['id', 'name']


@admin.register(Present)
class PresentAdmin(admin.ModelAdmin):
    model = Present
    list_display = ['id', 'teacher', 'lecture', 'university']
