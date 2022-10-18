
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(upload_to='images', blank=True,
                                processors=[Thumbnail(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)