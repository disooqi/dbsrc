from django import forms
from django.forms import ModelForm
from center.models import Contact


'''
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
'''
class ContactForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    
    class Meta:
        model = Contact
