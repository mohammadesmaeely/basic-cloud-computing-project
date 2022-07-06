from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Assessment(models.Model):
    registrar = models.CharField(max_length=200, verbose_name=_("registrant"))
    present = models.CharField(max_length=200, verbose_name=_("presenting lesson"))
    rate = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ],
        verbose_name=_("rate")
    )
    comment = models.TextField(verbose_name=_("comment"))

    class Meta:
        verbose_name = _("assessment")
        verbose_name_plural = _("assessments")

    def __str__(self):
        return f'{self.present} - {self.comment}'
