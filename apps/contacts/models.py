from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

# - first name
# - last name
# - email
# - phone number
class Contact(models.Model):
   first_name = models.CharField(max_length=64)
   last_name = models.CharField(max_length=64)
   email = models.EmailField()
   phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone should have the following format: '+xxxxxxxxx'.")
   phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)

   def __str__(self):
      return self.first_name + ' ' + self.last_name