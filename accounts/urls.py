from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.models import User

from accounts.views import ProfileView, SignupWizard
from accounts.forms import UserCreationForm_1, UserCreationForm_identity_info, UserCreationForm_contact_info

urlpatterns = patterns('accounts.views',
                       #url(r'^signup/$', 'create_user'),
                       url(r'^signup/done/$', 'user_creation_done', name = 'signup_done'),
                       
                       url(r'^signup/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
                        'signup_confirm'),

                       url(r'^signup/complete/$', 'signup_complete'),
                       url(r'^denied/$',
                           TemplateView.as_view(
                               template_name="registration/access_denied.html")),
                       url(r'^profile/$', ProfileView.as_view()),
                       url(r'^profile/edit/$', 'edit_user_information'),
                       url(r'^signup/step2/$', 'identityinfo', name="signup_step2"),
                       url(r'^signup/step3/$', 'contactinfo', name="signup_step3"),
                       url(r'^signup/$', SignupWizard.as_view([UserCreationForm_1, UserCreationForm_identity_info, UserCreationForm_contact_info])),

    )

urlpatterns += patterns('django.contrib.auth.views',
                       (r'^login/$', 'login'),
                       (r'^logout/$', 'logout'),
                       (r'^logout_then_login/$', 'logout_then_login'),
                       (r'^password_change/$', 'password_change'),
                       (r'^password_change/done/$', 'password_change_done'),
                       
                       (r'^password_reset/$', 'password_reset'),
                       (r'^password_reset/done/$', 'password_reset_done'),
                       (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm'),
                       (r'^reset/done/$', 'password_reset_complete'),                       
    )
