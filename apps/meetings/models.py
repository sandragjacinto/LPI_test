from django.db import models
from apps.contacts.models import Contact

# Create your models here.
# - title (name of the meeting)
# - description (free text field)
# - date (date and time of the meeting)
# - duration (in minutes)
# - contacts (you can have a meeting with several contacts)
# - status (completed, to do, canceled, etc.)

class Meeting(models.Model):
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField()
    date = models.DateTimeField()
    duration = models.IntegerField()
    contacts = models.ManyToManyField(Contact)
    status = models.CharField(max_length=10, choices=[('completed', 'completed'), ('todo', 'todo'), ('canceled', 'canceled'), ('inprogress', 'inprogress')], default='todo')

    def __str__(self):
      return self.title + ' ' + self.status
