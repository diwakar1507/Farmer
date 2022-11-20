from django.db import models

# Create your models here.
class Contact (models.Model):
    name = models.CharField(max_length=30, null=False,
   blank=False)
    mobile = models.CharField(max_length=10, null=True,
   blank=True)
    email = models.EmailField(null=True,
   blank=True)
    tractor = models.CharField(max_length=30, null=True,
   blank=True)
    details = models.TextField(null=True,
   blank=True)
    def __str__(self):
        return self.name
    