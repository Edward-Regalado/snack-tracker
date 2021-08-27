from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snacks(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=256, default=0)
    
    def __str__(self):
        return self.name[:50]