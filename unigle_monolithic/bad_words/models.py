from django.db import models
from django.utils.translation import gettext_lazy as _


class BadWord(models.Model):
    word = models.CharField(unique=True, max_length=300, verbose_name=_("word"))

    class Meta:
        verbose_name = _("bad word")
        verbose_name_plural = _("bad words")

    def __str__(self):
        return self.word
