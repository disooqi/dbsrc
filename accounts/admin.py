from django.contrib import admin
from accounts.models import Person
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin



admin.site.unregister(User)

class PersonInline(admin.StackedInline):
    model = Person

class PersonAdmin(UserAdmin):
	inlines = [PersonInline]

admin.site.register(User, PersonAdmin)
