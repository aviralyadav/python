from django.db import models
from tinymce.models import HTMLField

class Neww(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()

# Create your models here.
