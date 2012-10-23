from django.db import models
from django.forms import ModelForm
from accounts.models import Person

class Staff(Person):
    mname = models.CharField("Middle Name(s)", max_length=50)    
    position = models.CharField(max_length=200)    
    #image = models.ImageField()
    def __unicode__(self):
        return self.first_name + self.mname + self.last_name

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sender = models.EmailField("Email Address")

    def __unicode__(self):
        return self.subject

##################################   ModelForm   ##############################
class ContactForm(ModelForm):
    class Meta:
        model = Contact

