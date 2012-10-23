from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from center.models import Contact, ContactForm
from events.models import Article

def index(request):
    event_list = Article.objects.filter(show_in_home=True).order_by('-pub_date')[:5]
    return render_to_response('center/base_center.html', {'news_entries':event_list} ,
                              context_instance=RequestContext(request))
    #populate news

def contact(request):
##    if request.user.is_authenticated():
##        contact = Contact(sender = request.user.email)
##    else:
##        contact = None
    if request.method == 'POST':
        form = ContactForm(request.POST)      
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('center.views.showthankyou')) # Redirect after POST
    else:
        if request.user.is_authenticated():
            form = ContactForm(initial={'sender':request.user.email})
        else:
            form = ContactForm()
##        form = ContactForm(instance=contact) #old idea
##        data = {'subject':'a trial subject', 'message': 'a trial Message', 'sender': 'hi@df.df'}
##        form = ContactForm(data)


    return render_to_response('center/center_contact.html',
                              {'form': form,},
                              context_instance=RequestContext(request))

def showthankyou(request):
    return render_to_response('center/center_thanks.html',
                              context_instance=RequestContext(request))

#def show_about(request):
#    return render_to_response('center/base_center_about.html',
#                              context_instance=RequestContext(request))

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('center.views.showthankyou'))
    else:
        form = FeedbackForm()

    return render_to_response('center/center_feedback.html',
                              {'form':form},
                              context_instance=RequestContext(request))

def showStaff(request):
    return render_to_response('center/base_center_staff.html',
                              context_instance=RequestContext(request))

##########################  Class-based Generic Views  #############################
from django.views.generic import TemplateView

#this class replaces the show_about function
class AboutView(TemplateView):
    template_name = 'center/base_center_about.html'
























