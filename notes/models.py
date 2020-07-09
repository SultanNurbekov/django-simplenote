from django.db import models

 
class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    color = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
