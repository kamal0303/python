from django.db import models

# Create your models here.
# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name + self.email
