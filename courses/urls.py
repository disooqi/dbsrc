from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView
from courses.models import CourseType

urlpatterns = patterns('courses.views',
    url(r'^$', 'index'),
    url(r'^(?P<type_id>\d+)/$', 'showCourses'),
    url(r'^enroll/(?P<course_id>\d+)/$', 'enroll'),
    url(r'^enroll/thanks/$', TemplateView.as_view(template_name="courses/enroll_thanks.html")), 
    url(r'^student/(?P<student_id>\d+)/thanks/$', 'showthankyou'),
    url(r'^student/(?P<student_id>\d+)/update/$', 'updateStudentInfo'),
    url(r'^my_courses/$', 'show_courses_history'),
    url(r'^my_courses/1/$', TemplateView.as_view(template_name="courses/myCourseInfo.html")),
            
)
#url(r'^(?P<course_id>\d+)/course-info/$', 'showCourseInfo'),
#url(r'^available-courses/$', 'showAvailableCourses'),

urlpatterns += patterns('',
    url(r'^description/(?P<pk>\d+)/$', DetailView.as_view(
        model=CourseType,
        template_name='courses/coursetype_detail.html',
        context_object_name='type',
        )),
)

