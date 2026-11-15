from django.db import models

class Link(models.Model):

    def __str__(self):
        return self.name

    address = models.CharField(max_length=2000, null=False, blank=False)
    name = models.CharField(max_length=2000, null=False, blank=False)
