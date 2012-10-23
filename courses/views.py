from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
#the following import to get rid of the previous one
from django.shortcuts import render_to_response, get_object_or_404
#from django.http import Http404
from django.template import RequestContext
from courses.models import Student, Course, Enrollment, CourseType, CourseSession, Instructor
from accounts.models import Person
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    types = CourseType.objects.all()
    return render_to_response('courses/base_courses.html', {'courseTypes': types},
                              context_instance=RequestContext(request))

def in_students_group(user):
    if user:
        return user.groups.filter(name='students').count() > 0
    return False

@login_required
@user_passes_test(in_students_group, login_url='/accounts/denied/')
def enroll(request, course_id):
    try:
        s = request.user.person.student
    except ObjectDoesNotExist:
        s = Student.objects.create(person = request.user.person)

    #here check for his data

    c = get_object_or_404(Course, pk=course_id)
    e = Enrollment(course = c, student = s)
    e.save()
    return HttpResponseRedirect('/courses/enroll/thanks/')
        
    #this need to be more fast by making it probrty 
    if len(Student.objects.filter(person__pk = request.user.id)) > 0:
        return HttpResponse('thanks')
    else:
        p = get_object_or_404(Person, pk = request.user.id)
        ####################################################
        s = Student.objects.create(person=p)
        return HttpResponse('you are now a student')
        
    #change his permission to be student
    #check if the information is complete

@login_required
@user_passes_test(in_students_group, login_url='/accounts/denied/')
def show_courses_history(request):
    courses_history = {'C++':[2, 6, 7]}
    return render_to_response('courses/enrolled_courses.html', {'courses_history': courses_history},
                              context_instance=RequestContext(request))

def updateStudentInfo(request, student_id):
    s = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=s)
        
        if form.is_valid():
            s.save()
            return HttpResponseRedirect('/courses/student/'+str(student_id)+'/thankyou/')
    else:
        form = StudentForm(instance=s)
    return render_to_response('courses/course_updatestudentinfo.html', {
        'form': form,
        'student_id':student_id,    
    }, context_instance=RequestContext(request))


def showCourses(request, type_id):
    courseType = get_object_or_404(CourseType, pk=type_id)
    courseInstances = Course.objects.filter(course_type_id__exact=type_id)
    sessions = {}
    for instance in courseInstances:
        sessions[instance] = CourseSession.objects.filter(course_id__exact=instance.id)
    

    return render_to_response('courses/base_course_instances.html',
                              {'courseInstances':courseInstances,
                               'type':courseType,
                               'schedule':sessions}, context_instance=RequestContext(request))

def showCourseInfo(request, course_id):
    c = get_object_or_404(Course, pk=course_id)
    return render_to_response('courses/course-info.html', {'course': c})


def showthankyou(request, student_id):
    return render_to_response('courses/base_course_thankyou.html', {'student_id':student_id})

def viewCalender(request):
    pass

