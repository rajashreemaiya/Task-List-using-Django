from django.db import models

class Item(models.Model):

    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
