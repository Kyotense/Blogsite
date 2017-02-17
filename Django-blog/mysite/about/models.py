from __future__ import unicode_literals

from django.db import models
from PIL import Image

def user_directory_path(instance, filename):
    return '%s/%s' %(instance.id, filename)

class AboutUs(models.Model):
    name = models.CharField(max_length=140)
    pic = models.ImageField(upload_to = user_directory_path)
    description = models.TextField()

    def __unicode__(self):
        return self.name
