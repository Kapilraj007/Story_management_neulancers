from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Story_Management(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt =models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createdAt','-updatedAt']
    
    def __str__(self):
        return self.title