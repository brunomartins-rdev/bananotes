from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=200)
    is_archived = models.BooleanField()
    color = models.CharField()
    created_at = models.DateField()
    updated_at = models.DateField()

