from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class Neww(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    news_image = models.FileField(upload_to='news/', max_length=250, null=True, default=None)
    news_slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)

# Create your models here.
