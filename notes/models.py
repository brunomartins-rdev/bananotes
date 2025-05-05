from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    is_archived = models.BooleanField()
    color = models.CharField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField()

    def __str__(self):
        return self.title

