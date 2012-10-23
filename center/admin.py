from center.models import Contact, Staff
from django.contrib import admin

class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['subject']}),
        (None, {'fields': ['message']}),
        (None, {'fields': ['sender']}),
    ]
    list_display =('subject', 'message', 'sender')





admin.site.register(Contact, ContactAdmin)
admin.site.register(Staff)

