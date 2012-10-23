from courses.models import Instructor, CourseType, Course, Student, Enrollment, CourseSession
from django.contrib import admin

#admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(CourseType)
'''
class CourseInline(admin.TabularInline):
    model = Course
    extra = 1

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1

class ScheduleInline(admin.TabularInline):
    model = CourseSession
    extra = 1

class InstructorAdmin(admin.ModelAdmin):
    fieldsets = [
        
        (None, {'fields': ['gender']}),
        (None, {'fields': ['dob']}),
        (None, {'fields': ['cellular']}),
        (None, {'fields': ['home_phone']}),
        (None, {'fields': ['address']}),
        #(None, {'fields': ['user.email']}),
        (None, {'fields': ['social_id']}),
        (None, {'fields': ['academic_qualification']}),
        (None, {'fields': ['university']}),
        (None, {'fields': ['comment']}),
    ]
    inlines = [CourseInline]
    list_display =('user', 'gender', 'dob', 'cellular', 'home_phone', 'address', 'email', 'social_id',
                   'academic_qualification', 'university', 'comment')

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        (None, {'fields': ['gender']}),
        (None, {'fields': ['dob']}),
        (None, {'fields': ['cellular']}),
        (None, {'fields': ['home_phone']}),
        (None, {'fields': ['address']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['social_id']}),
        (None, {'fields': ['academic_qualification']}),
        (None, {'fields': ['university']}),
        (None, {'fields': ['occupation']}),
        (None, {'fields': ['employer']}),
        (None, {'fields': ['comment']}),
    ]
    inlines = [EnrollmentInline]
    list_display =('user', 'gender', 'dob', 'cellular', 'home_phone', 'address', 'email', 'social_id',
                   'academic_qualification', 'university', 'occupation', 'employer', 'comment')

class CourseTypeAdmin(admin.ModelAdmin):
        fieldsets = [
        (None, {'fields':['title']}),
    ]
    
class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['title']}),
        (None, {'fields': ['instructor']}),
        ('Date Information', {'fields':['start_date', 'end_date'], 'classes':['collapse']}),
        (None, {'fields':['hours']}),
        (None, {'fields':['place']}),
        (None, {'fields':['fees']}),
    ]
    inlines = [EnrollmentInline, ScheduleInline]
    #inlines = [ScheduleInline]
    
    list_display = ('title', 'instructor', 'start_date', 'end_date', 'hours', 'place', 'fees')
    list_filter = ['start_date']
    search_fields = ['title']

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(CourseType, CourseTypeAdmin)
'''

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms.models import inlineformset_factory


def upgrade_user_admin(UserProfile):
    class UserProfileFormSet(inlineformset_factory(User, UserProfile)):
        def __init__(self, *args, **kwargs):
            super(UserProfileFormSet, self).__init__(*args, **kwargs)
            self.can_delete = False
    
    # Allow user profiles to be edited inline with User
    class UserProfileInline(admin.StackedInline):
        model = UserProfile
        fk_name = 'user'
        max_num = 1
        extra = 0
        formset = UserProfileFormSet
    
    class MyUserAdmin(UserAdmin):
        inlines = [UserProfileInline, ]
        actions = ['make_active', 'make_inactive',]
        list_filter = ['is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login',]
        list_display = ['first_name', 'last_name', 'email', 'username', 'date_joined',]
        list_display_links = ['first_name', 'last_name', 'email', 'username']
        
        def make_active(self, request, queryset):
            rows_updated = queryset.update(is_active=True)
            if rows_updated == 1:
                message_bit = "1 person was"
            else:
                message_bit = "%s people were" % rows_updated
            self.message_user(request, "%s successfully made active." % message_bit)
    
        def make_inactive(self, request, queryset):
            rows_updated = queryset.update(is_active=False)
            if rows_updated == 1:
                message_bit = "1 person was"
            else:
                message_bit = "%s people were" % rows_updated
            self.message_user(request, "%s successfully made inactive." % message_bit)


    # Re-register UserAdmin
    admin.site.unregister(User)
    admin.site.register(User, MyUserAdmin)
    
upgrade_user_admin(Instructor)

