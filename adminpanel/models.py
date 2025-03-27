from django.db import models

class App(models.Model):
    name = models.CharField(max_length=255)
    package_name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
