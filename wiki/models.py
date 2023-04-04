from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SavedSearch(models.Model):
    query = models.CharField(max_length=600)
    result = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.query} ({self.user.username}, {self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"

