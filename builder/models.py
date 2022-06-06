from django.db import models

# Create your models here.

class Education(models.Model):
    school_name = models.CharField(max_length= 50)
    school_location = models.TextField()
    degree = models.CharField(max_length=10)
    major = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

class Profile(models.Model):
    full_name = models.CharField(max_length= 25)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    link = models.URLField(max_length= 150)

    def __str__(self) -> str:
        return "{} - {} - {}".format(self.full_name, self.email, self.phone_number)
