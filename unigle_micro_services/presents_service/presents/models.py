from django.db import models
from django.utils.translation import gettext_lazy as _


# class State(models.Model):
#     name = models.CharField(unique=True, max_length=200, verbose_name=_("name"))
#
#     class Meta:
#         verbose_name = _("state")
#         verbose_name_plural = _("states")
#
#     def __str__(self):
#         return self.name
#
#
# class City(models.Model):
#     name = models.CharField(max_length=100, verbose_name=_("name"))
#     state = models.ForeignKey(State, on_delete=models.PROTECT, verbose_name=_("state"))
#
#     class Meta:
#         verbose_name = _("city")
#         verbose_name_plural = _("cities")
#         unique_together = ['name', 'state']
#
#     def __str__(self):
#         return self.name


class University(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("name"))
    # city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='شهر')

    class Meta:
        verbose_name = _("university")
        verbose_name_plural = _("universities")

    def __str__(self):
        return self.name


class Lecture(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("name"))

    class Meta:
        verbose_name = _("lecture")
        verbose_name_plural = _("lectures")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("name"))
    image = models.ImageField(upload_to='static/images/teacher_image', null=True, blank=True, verbose_name=_("image"))

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")

    def __str__(self):
        return self.name


class Present(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=_("teacher"))
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, verbose_name=_("lecture"))
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name=_("university"))

    class Meta:
        verbose_name = _("presenting lesson")
        verbose_name_plural = _("lesson presentations")

    def __str__(self):
        return self.teacher.name + "-->" + self.lecture.name
