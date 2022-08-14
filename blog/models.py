from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return self.title