from django.db import models

# Create your models here.


class Snippet(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    language = models.CharField(max_length=30, blank=False, null=False)
    code_snippet = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=50, blank=False, null=False)

