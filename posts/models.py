from django.db import models
from django.utils import timezone

class Post(models.Model):
  class Meta:
    db_table = 'posts'

  content = models.CharField(max_length=255,blank=True)
  created_at = models.DateTimeField(default=timezone.now)

# Create your models here.
