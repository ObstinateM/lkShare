from django.db import models

# Create your models here.

class lk(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.url