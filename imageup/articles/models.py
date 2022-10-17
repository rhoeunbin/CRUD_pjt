from email import contentmanager
from email.mime import image
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = ImageSpecField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[Thumbnail(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
