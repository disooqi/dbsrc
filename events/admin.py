from events.models import Article
from django.contrib import admin

admin.site.register(Article)
#admin.site.register(Choice)

############################################################
#class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question', 'isCurrent']
#
#admin.site.register(Poll, PollAdmin)
#
############################################################
#class ChoiceInline(admin.StackedInline):
#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 1
#
#class PollAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date']}),
#        ('is the Poll the current one', {'fields': ['isCurrent'],
#                                         'classes': ['collapse']}),
#    ]
#    inlines = [ChoiceInline]
#
#    #By default, Django displays the str() of each object.
#    #But sometimes it'd be more helpful if we could display individual fields. 
#   list_display = ('question', 'pub_date', 'was_published_recently')
#
#admin.site.register(Poll, PollAdmin)
