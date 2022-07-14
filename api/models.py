from django.db import models

LOC_CHOICE =((
    ("bahawalpur", 'Bahawalpur'),
    ('lahore', 'Lahore'),
    ('islamabad', "Islamabad"),
    ('karachi', 'Karachi')

))

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    loc = models.CharField(choices=LOC_CHOICE, max_length=50)
    gender = models.CharField(max_length=100)
    pjl = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='pimages', blank=True)
    file = models.FileField(upload_to='fileDoc', blank=True)