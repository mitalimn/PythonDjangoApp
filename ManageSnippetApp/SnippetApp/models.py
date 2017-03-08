from django.db import models

# Create your models here.


class Snippet(models.Model):
    title = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    code_snippet = models.CharField(max_length=50)
    description = models.CharField(max_length=50);