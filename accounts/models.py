from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


GENDER_CHOICES = (
    (u'M', u'Male'),
    (u'F', u'Female'),
    )
class Person(models.Model):
    user = models.OneToOneField(User, primary_key = True)
    
    #second_name = models.CharField("Father's Name", max_length=30, null=True, blank = True)
    #third_name = models.CharField("Grandfather's Name", max_length=30, null=True, blank = True)
    
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    dob = models.DateField("Date of birth", null=True, blank = True)
    #changed
    social_id = models.CharField(max_length=14, unique=True)
    #make it country with defined list of countries 195 including phalstine and no the zuinsit entity
    country = models.CharField(max_length=20)
    academic_qualification = models.CharField("Academic qualification", max_length=150, null=True, blank = True)
    university = models.CharField(max_length=100, null=True, blank = True)

    cellular = models.CharField("Mobile phone", max_length=15)    
    home_phone = models.CharField(max_length=15, null=True, blank = True)
    address = models.CharField(max_length=200, null=True, blank = True)
    
    comment = models.TextField(null=True, blank = True)
    
    def __unicode__(self):
        return self.user.username

##################################
def create_person(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)

post_save.connect(create_person, sender=User)
