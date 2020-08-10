from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    time_duration = models.IntegerField()

    def __str__(self):
        return self.name