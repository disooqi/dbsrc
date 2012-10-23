from django.db import models
from courses.models import Course


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateField()
    issued_by = models.CharField(max_length=100, null= True, blank=True)
    expire_date = models.DateField(null= True, blank=True)
    right_to_left = models.BooleanField() #make it rtl and make its text "right to left"
    show_in_home = models.BooleanField()
    course = models.ForeignKey(Course, null= True, blank=True)
    ## if belongs to certain course, give the instructor to send it
    ## to all student
    
    #image = models.ImageField()

    def __unicode__(self):
        return self.title

