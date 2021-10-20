from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    due_date = models.DateTimeField()
    is_complete = models.BooleanField(default=False)

