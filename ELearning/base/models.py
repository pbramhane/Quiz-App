from django.db import models

# Create your models here.
class Notes(models.Model):
    note_title = models.CharField(max_length=250)
    note_desc = models.TextField()

    def __str__(self):
        return self.note_title