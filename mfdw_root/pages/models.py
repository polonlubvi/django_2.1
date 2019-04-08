from django.db import models

# Create your models here.
class Page(model.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)
