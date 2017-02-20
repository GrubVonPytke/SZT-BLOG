# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class News(models.Model):
    content = models.TextField(max_length=150, verbose_name="Zawartosc")
    published = models.DateTimeField(verbose_name="Data publikacji")

    def __unicode__(self):
        return self.content
