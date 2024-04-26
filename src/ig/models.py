from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    # poster
    

    def __str__(self) -> str:
        return self.message