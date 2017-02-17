from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title
