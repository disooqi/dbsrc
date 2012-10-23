from courses.models import Instructor, CourseType, Course, Student, Enrollment, CourseSession
from django.contrib import admin



class CourseSessionInline(admin.TabularInline):
    model = CourseSession
    extra = 1

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseSessionInline, EnrollmentInline]
    list_display = ('course_type', 'start_date', 'end_date', 'is_course_enrollment_available', 'number_of_enrolled_students')
    #list_filter = ['pub_date']
    #search_fields = ['question']
    #date_hierarchy = 'pub_date'

admin.site.register(Course, CourseAdmin)





admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(CourseType)

