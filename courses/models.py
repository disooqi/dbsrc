from django.db import models
from accounts.models import Person
from django.db.models.signals import post_save
from django.contrib.auth.models import Group, Permission
import datetime
from django.utils import timezone

class Instructor(models.Model):
    person = models.OneToOneField(Person, primary_key=True)
    def __unicode__(self):
        return self.person.user.first_name + " " + self.person.user.last_name

class Student(models.Model):
    person = models.OneToOneField(Person, primary_key=True)
    
    occupation = models.CharField(max_length=100, null=True, blank = True)
    employer = models.CharField(max_length=100, null=True, blank = True)

    def __unicode__(self):
        return self.person.user.first_name + " " + self.person.user.last_name
         
class CourseType(models.Model):
    title = models.CharField(max_length=200)
    intro = models.TextField("Introduction", null=True, blank = True)
    objective = models.TextField('Aim of the Course', null=True, blank = True)
    syllabus = models.TextField(null=True, blank = True)
    pre = models.TextField("Prerequisites", null=True, blank = True)
    aud = models.TextField("Intended Audience", null=True, blank = True)
    readings = models.TextField("Textbook and Readings", null=True, blank = True)
    
    
    def __unicode__(self):
        return self.title

class Course(models.Model):
    students = models.ManyToManyField(Student, through='Enrollment')
    
    instructor = models.ForeignKey(Instructor)
    course_type = models.ForeignKey(CourseType)
    
    start_date = models.DateField()
    end_date = models.DateField()

    hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank = True)
    place = models.CharField(max_length=10)
    fees = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank = True)
    min_student = models.IntegerField('Minimum number of Students Required', null=True, blank = True,
                                      help_text='Minimum number of Students Required to start the course')
    max_student = models.IntegerField('Maximum number of Students', null=True, blank = True,
                                      help_text='Maximum number of Students the course can have')
    isExam = models.BooleanField("Exam Availability?")
    

    def __unicode__(self):
        return self.course_type.title

    def has_course_ended(self):
        return self.end_date <= timezone.now().date()

    def number_of_enrolled_students(self):
        #return 6
        return Student.enrollment.filter(test__exact ='P').count()
        #self.students.objects.filter(members__name__startswith='Paul')
        #return self.students.enrollment.filter(nrollment_status='P').count()
        #return self.objects.filter(enrollment_nrollment_status='P').count()
    

    number_of_enrolled_students.short_description = 'Enrolled students'
    
    def can_start(self):
        pass
    def place_for_enroll(self):
        pass

    def is_course_enrollment_available(self):
        return not self.has_course_ended() # and  25 == self.max_student

    is_course_enrollment_available.short_description = 'Available for enrollment?'
    is_course_enrollment_available.boolean = True

    

class CourseSession(models.Model):
    date = models.DateTimeField(null=True, blank = True)
    period = models.DecimalField(max_digits=4, decimal_places=2)
    
    students = models.ManyToManyField(Student, through='Attendance')
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.date.isoformat()

class Exam(models.Model):
    max_degree = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank = True)
    pass_degree = exam_result = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank = True)
    exam_result = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank = True)
    note = models.CharField(max_length=50, null=True, blank = True)

    def __unicode__(self):
        return exam_result

ENROLLMENT_STATUS_CHOICES = (
    ('G', 'Grace Period'),
    ('P', 'Paid'),
    ('W', 'Waiting'),
    ('C', 'Cancelled'),
)
class Enrollment(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    enrollmentStatus = models.CharField(max_length=1, choices=ENROLLMENT_STATUS_CHOICES, default='G')
    exam = models.ForeignKey(Exam, null=True, blank = True)
    test = models.CharField(max_length=1)
    #attendance = models.IntegerField(null=True, blank = True)

class Attendance(models.Model):
    student = models.ForeignKey(Student)
    session = models.ForeignKey(CourseSession)
    attendanceStatus = models.BooleanField("Attended?", default = False)
#################################################################################################
    
def add_to_students_group(sender, instance, created, **kwargs):
    if created:
        instance.person.user.groups.add(Group.objects.get(name='students'))

post_save.connect(add_to_students_group, sender=Student)


'''
def add_to_instructors_group(sender, instance, created, **kwargs):
    if created:
        instance.person.user.groups.add(Group.objects.get(name='instructors'))

post_save.connect(add_to_instructors_group, sender=Instructor)
'''
