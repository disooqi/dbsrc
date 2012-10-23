from center.models import Article, Contact, Staff, Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['content']}),
        (None, {'fields': ['pub_date']}),
        (None, {'fields': ['issued_by']}),
    ]
    list_display =('title', 'content', 'pub_date', 'issued_by')

class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['subject']}),
        (None, {'fields': ['message']}),
        (None, {'fields': ['sender']}),
    ]
    list_display =('subject', 'message', 'sender')

class StaffAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['position']}),
        #('Name', {'fields':['first_name', 'mname', 'last_name'], 'classes':['collapse']}),
        (None, {'fields': ['position']}),
        (None, {'fields': ['dob']}),
        #(None, {'fields': ['email']}),
        (None, {'fields': ['cellular']}),
        (None, {'fields': ['home_phone']}),
        (None, {'fields': ['comment']}),
    ]
    list_display =('fname', 'mname', 'lname', 'position', 'dob', 'email', 'cellular', 'home_phone', 'comment')

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        (None, {'fields': ['pub_date']}),
        (None, {'fields': ['current']}),
    ]
    inlines = [ChoiceInline]
    list_display =('question', 'pub_date', 'current')

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['poll']}),
        (None, {'fields': ['choice_text']}),
        (None, {'fields': ['vote_count']}),
    ]
    list_display =('poll', 'choice_text', 'vote_count')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
