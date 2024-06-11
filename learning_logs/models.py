from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """creating user's topic"""
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """returning and showing the text"""
        return self.text
    
class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text)>=30:
            return self.text[:30] + "..."
        else:
            return self.text