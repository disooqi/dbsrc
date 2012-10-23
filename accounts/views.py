from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.sites.models import Site
from django.contrib.formtools.wizard.views import SessionWizardView

from accounts.forms import UserCreationForm_1, EditPersonInformation, UserCreationForm_identity_info, UserCreationForm_contact_info

from accounts.models import Person
from courses.models import Student

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings

from django.views.generic import TemplateView

from django.utils.http import urlquote, base36_to_int
from django.utils.decorators import method_decorator


class SignupWizard(SessionWizardView):
    def done(self, form_list, **kwargs):
        #do_something_with_the_form_data(form_list)
        opts = {}
        opts['use_https'] = self.request.is_secure()
        opts['token_generator'] = default_token_generator
        opts['email_template_name'] = 'registration/signup_email.html'
        opts['first_name'] = form_list[1].cleaned_data['first_name']
        opts['last_name'] = form_list[1].cleaned_data['last_name']
        if not Site._meta.installed:
            opts['domain_override'] = RequestSite(self.request).domain
        user = form_list[0].save(**opts)
        
        person = user.get_profile()
        person.social_id = form_list[1].cleaned_data['social_id']
        person.dob = str(form_list[1].cleaned_data['dob_year']) + '-'\
                        + str(form_list[1].cleaned_data['dob_month']) + '-'\
                        + str(form_list[1].cleaned_data['dob_day'])
        
        person.gender = form_list[1].cleaned_data['gender']
        person.country = form_list[1].cleaned_data['country']
        person.academic_qualification = form_list[1].cleaned_data['academic_qualification']
        person.cellular = form_list[2].cleaned_data['cellular']
        person.home_phone = form_list[2].cleaned_data['home_phone']
        person.address = form_list[2].cleaned_data['address']
        
        person.save()

        #p = Person(**pers_args)
        #user.person(instance = p)

        #form_list[1].update(form_list[2])
        #form_list[1].save()
        return HttpResponseRedirect('/accounts/signup/done/')
        #return render_to_response('done.html', {'form_data': [form.cleaned_data for form in form_list]})
    
    def get_context_data(self, form, **kwargs):
        context = super(SignupWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == 'my_step_name':
            context.update({'another_var': True})
        return context


def create_user(request):
    if request.method == "POST":
        form = UserCreationForm_1(request.POST)
        if form.is_valid():
            opts = {}
            opts['use_https'] = request.is_secure()
            opts['token_generator'] = default_token_generator
            opts['email_template_name'] = 'registration/signup_email.html'
            if not Site._meta.installed:
                opts['domain_override'] = RequestSite(request).domain
            user = form.save(**opts)
    
            return HttpResponseRedirect(reverse('signup_step2'))
            
    else:
        form = UserCreationForm_1()

    return render_to_response('registration/signup.html', {'form': form},
                              context_instance=RequestContext(request))

def identityinfo(request):
    if request.method == "POST":
        id_info_form = UserCreationForm_identity_info(request.POST)
        if id_info_form.is_valid():
            return HttpResponseRedirect(reverse('signup_step3'))
    else:
        id_info_form = UserCreationForm_identity_info()
        
    return render_to_response('registration/signup_id.html', {'form': id_info_form},
                              context_instance=RequestContext(request))

def contactinfo(request):
    if request.method == "POST":
        contact_info_form = UserCreationForm_contact_info(request.POST)
        if contact_info_form.is_valid():
            return HttpResponseRedirect(reverse('signup_done'))
    else:
        contact_info_form = UserCreationForm_contact_info()
        
    return render_to_response('registration/signup_contact.html', {'form': contact_info_form},
                              context_instance=RequestContext(request))


def user_creation_done(request):
    return render_to_response('registration/signup_done.html', 
                              context_instance=RequestContext(request))

@login_required
def user_creation_step_two(request):
    person = request.user.get_profile()

    if request.POST:
        step_two_form = PersonCreation_StepTwo_Form(request.POST)
        if step_two_form.is_valid():
            request.user.first_name = request.POST['first_name']
            request.user.last_name = request.POST['last_name']
            person.second_name = request.POST['second_name']
            person.third_name = request.POST['third_name']
            person.cellular = request.POST['cellular']

            request.user.save()
            person.save()
            #step_two_form.save()
            return HttpResponseRedirect(reverse('accounts.views.signup_complete'))            
    else:
        step_two_form = PersonCreation_StepTwo_Form(instance = person)
        
    return render_to_response('registration/signup_step_two.html',
                              {'form':step_two_form}, 
                              context_instance=RequestContext(request))


def signup_confirm(request, uidb36=None, token=None,
                   token_generator=default_token_generator,
                   post_signup_redirect=None):
    assert uidb36 is not None and token is not None #checked par url
    try:
        uid_int = base36_to_int(uidb36)
    except ValueError:
        raise Http404

    user = get_object_or_404(User, id=uid_int)
    context_instance = RequestContext(request)

    if token_generator.check_token(user, token):
        context_instance['validlink'] = True
        user.is_active = True
        user.save()
        s = Student.objects.create(person = user.person)
        if request.user != user:
            logout(request)
    else:
        context_instance['validlink'] = False
    return HttpResponseRedirect('/accounts/signup/complete/')


def signup_complete(request):
    return render_to_response('registration/signup_complete.html', 
                              context_instance=RequestContext(request))

@login_required
def edit_user_information(request):
    if request.method == "POST":
        user_form = UserChangeForm(request.POST)
        person_form = EditPersonInformation(request.POST)
        try:
            s = request.user.person.student
        except ObjectDoesNotExist:
            pass
        try:
            i = request.user.person.instructor
        except ObjectDoesNotExist:
            pass
    else:
        user_form = UserChangeForm(instance=request.user)
        person_form = EditPersonInformation(instance=request.user.person)
    return render_to_response('registration/edit_user_information.html',
                              {'user_form':user_form,'person_form':person_form,},
                              context_instance=RequestContext(request))


class ProfileView(TemplateView):
    template_name = "registration/profile.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileView, self).dispatch(*args, **kwargs)


