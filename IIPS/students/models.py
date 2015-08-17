from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from iips_site.models import Faculty_Info, Course

# Create your models here.


class Student(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Batch = models.ForeignKey('Batch')
    Father_Name =models.CharField(max_length=200)
    Mother_Name =models.CharField(max_length=200)
    DOB= models.DateField(max_length=200)
    Local_Address =models.CharField(max_length=200,default=None,blank=True)
    Permanent_Address =models.CharField(max_length=200,default = None)
    Mobile_Number =models.CharField(max_length=15,blank=True)
    Telephone_Number =models.CharField(max_length=200,default=None,blank=True)
    Roll_Number =models.CharField(max_length=200,default = None)
    Enrollment_Number =models.CharField(max_length=200,default=None)
    Picture=models.URLField(default=None,blank=True)

    def __unicode__(self):  # Python 3: def __str__(self):
		return self.User.username

class Batch(models.Model):
	Semester=models.CharField(max_length=15)
	Course=models.ForeignKey(Course)
	Faculty =  models.ManyToManyField(Faculty_Info, verbose_name=_('faculties'), blank=True
    )
	Room_Number = models.CharField(max_length=5)

	def __unicode__(self):  # Python 3: def __str__(self)
		return str(self.Course.name + ' ' + self.Semester)