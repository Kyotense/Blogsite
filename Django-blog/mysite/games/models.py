from __future__ import unicode_literals
from PIL import Image
from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    return '%s/%s' %(instance.id, filename)

class VideoGame(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, default="")
    logo = models.ImageField(upload_to = user_directory_path)
    platform = models.CharField(max_length=140)
    releasedate = models.CharField(max_length=140)
    description = models.TextField()

    def __unicode__(self):
        return self.title
