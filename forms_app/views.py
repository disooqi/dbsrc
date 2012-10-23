from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms_app.forms import ContactForm



def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass

            ##################################################
            # Process the data in form.cleaned_data
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)

            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            ###################################################
            
            return HttpResponseRedirect('/forms/thanks/') # Redirect after POST
    else: #for GET form; this happens when I open the page for the first time
        data = {'subject': 'hello', 'message': 'Hi there', 'sender': 'foo@example.com', 'cc_myself': True}
        form = ContactForm(data) # An unbound form

    return render(request, 'forms/forms_trial.html',
                  {'contact_form': form, }    # context variables
                  )
