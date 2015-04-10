from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Program(models.Model):
	name=models.CharField(max_length=30)
	def __unicode__(self):  # Python 3: def __str__(self)
		return self.name

class Course(models.Model):

	DISCIPLINE_CHOICES = (
        ('TECHNICAL', 'Technical'),
        ('MANAGEMENT', 'Management'),
    )
    
	
	name = models.CharField(max_length=200)
	program = models.ForeignKey('Program')
	number_of_semester = models.PositiveSmallIntegerField(null=True)
	Discipline = models.CharField(max_length=12, choices=DISCIPLINE_CHOICES, default='MANAGEMENT')
	description = models.TextField(max_length=2000,null=True)
	objective = models.TextField(max_length=2000,null=True)
	learning_outcomes = models.TextField(max_length=2000,null=True)
	
	def __unicode__(self):  # Python 3: def __str__(self)
		return self.name

	
	

# Table structure for table Sylabus


class Syllabus(models.Model):
	Semester=models.CharField(max_length=15)
	Course=models.ForeignKey('Course')
	def __unicode__(self):  # Python 3: def __str__(self)
		return str(self.Semester)


class Subject(models.Model):
	Course=models.ForeignKey(Syllabus)
	Subject_Name=models.CharField(max_length=40)
	Subject_ID=models.CharField(max_length=10,primary_key=True)
	Aim_Of_course=models.TextField(max_length=400)
	Objective=models.TextField(max_length=400)

	def __unicode__(self):  # Python 3: def __str__(self)
		return self.Course

	

class Course_Content(models.Model):
	Subject = models.ForeignKey(Subject)
	Unit=models.PositiveSmallIntegerField()
	Contents=models.CharField(max_length=400)

	def __unicode__(self):  # Python 3: def __str__(self)
		return self.Subject


#Table structure for table `User_Temp`

class User_Temp(models.Model):
	#Temp_Transaction_ID= varchar(10) NOT NULL COMMENT #'This is a temporary transaction id of the user.',
	First_Name= models.CharField(max_length=200,null =False)
	Last_Name =models.CharField(max_length=200,null =False)
	Father_Name =models.CharField(max_length=200)
	Mother_Name =models.CharField(max_length=200)
	Email =models.CharField(max_length=200)
	Type =models.CharField(max_length=200)
	DOB= models.DateField(max_length=200)
	Local_Address =models.CharField(max_length=200,default=None)
	Permanent_Address =models.CharField(max_length=200,default = None)
	Mobile_Number =models.CharField(max_length=15)
	Telephone_Number =models.CharField(max_length=200,default=None)
	Roll_Number =models.CharField(max_length=200,default = None)
	Enrollment_Number =models.CharField(max_length=200,default=None)
	Discipline =models.CharField(max_length=200)
	Post =models.CharField(max_length=200)
	Responsibility =models.CharField(max_length=200)
	Batch_ID =models.CharField(max_length=200,default=None)
	Course_ID =models.SmallIntegerField()
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.First_Name
	#PRIMARY KEY (`Temp_Transaction_ID`)
	

#Table structure for table `Staff_Info`
class StaffInfo(models.Model):
	User_ID=models.SmallIntegerField(max_length=6)
	Name=models.CharField(max_length=50)
	Post=models.CharField(max_length=40)
	Responsibility=models.CharField(max_length=40)
	Web_Link=models.CharField(max_length=40,default=None)
	Blog_Link=models.CharField(max_length=40,default=None)
	Alternate_Email=models.CharField(max_length=40,default=None)
	Linkedin_Link=models.CharField(max_length=40,default=None)
	Facebook_Link=models.CharField(max_length=40,default=None)
	Googleplus_Link=models.CharField(max_length=40,default=None)
	Twitter_Link=models.CharField(max_length=40,default=None)
	Picture=models.CharField(max_length=100,default=None)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Name

#Table structure for table `Faculty_Info`

class Faculty_Info(models.Model):
	User_ID=models.SmallIntegerField(max_length=6)#This is the user_id from User_master table.
	Name=models.CharField(max_length=50)
	Discipline =models.CharField(max_length=200)
	Designation=models.CharField(max_length=200)
	Responsibility=models.CharField(max_length=200)
	DOJ=models.DateField() 		#Date of Joining
	Qualification=models.CharField(max_length=200)
	Area_Of_Interest=models.CharField(max_length=200)
	Previous_Job=models.CharField(max_length=200)
	Web_Link=models.CharField(max_length=40,default=None)
	Blog_Link=models.CharField(max_length=40,default=None)
	Alternate_Email=models.CharField(max_length=40,default=None)
	Linkedin_Link=models.CharField(max_length=40,default=None)
	Facebook_Link=models.CharField(max_length=40,default=None)
	Googleplus_Link=models.CharField(max_length=40,default=None)
	Twitter_Link=models.CharField(max_length=40,default=None)
	Picture=models.CharField(max_length=100,default=None)
	Resume =models.CharField(max_length=40,default=None)#Link to resume
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Name


#Table structure for Admission Module


class Admission(models.Model):
	Block = models.CharField(max_length=25)
	def __unicode__(self):  # Python 3: def __str__(self)
		return self.Block


class Admissionblock(models.Model):
	Block = models.ForeignKey('Admission')
	Heading = models.CharField(max_length=50)
	Description = models.TextField(max_length=1000)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Heading

class Fee_Structure(models.Model):
	Course_Name=models.CharField(max_length=40,primary_key=True)
	School_Of_Studies=models.CharField(max_length=60,default="International Institute of Professional Studies(IIPS)")
	Group=models.CharField(max_length=1)
	Fees_Excluding_Student_Services_Fee=models.PositiveSmallIntegerField()
	Caution_Money_Refundable=models.PositiveSmallIntegerField()

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Course_Name

class Gallary(models.Model):
	photo = models.ImageField(upload_to='documents/gallary/')

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.photo.name 

'''
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/documents/gallary')

class Car(models.Model):
    ...
    photo = models.ImageField(storage=fs)
 '''

class News(models.Model):
	Title = models.CharField(max_length=100)
	Docfile = models.FileField(upload_to='documents/news/')
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Title

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Notification(models.Model):
	Title = models.CharField(max_length=100)
	Link = models.URLField()
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Title

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Calendar(models.Model):
	pass

class Placement(models.Model):
	Company = models.CharField(max_length=30)
	Course_Or_Specialization = models.CharField(max_length=20)
	Offers = models.PositiveSmallIntegerField()
	Package = models.DecimalField(max_digits=4, decimal_places=2)
	Discipline = models.ForeignKey('Placement_Detail')



class Placement_Detail(models.Model):
	
	
	DISCIPLINE_CHOICES = (
        ('TECHNICAL', 'Technical'),
        ('MANAGEMENT', 'Management'),
    )
    
	Discipline = models.CharField(max_length=12, choices=DISCIPLINE_CHOICES, default='MANAGEMENT')
	Detail = models.TextField(max_length=50)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Discipline

class Placement_Company(models.Model):
	
	Logo = models.ImageField(upload_to='documents/placement_company_logo/')

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Logo.name 

class Placement_Cell(models.Model):
	Name = models.CharField(max_length=50)
	Photo = models.ImageField(upload_to='documents/placementcell/')
	Designation = models.CharField(max_length=30)
	Contact_No = models.CharField(max_length=18)
	Email = models.EmailField()

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Name 

class About_IIPS(models.Model):
	Heading = models.CharField(max_length=50)
	Description = models.TextField(max_length=1000)
	def __unicode__(self):  
		return self.Heading

class Director(models.Model):
	Name = models.CharField(max_length=40)
	Working_Period = models.CharField(max_length=40)

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Name

class Director_Message(models.Model):
	Director = models.CharField(max_length=40)
	Message = models.TextField(max_length=1000)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Director

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	
class Vision_Mission_Goal(models.Model):
	Heading = models.CharField(max_length=50)
	Description = models.TextField(max_length=1000)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Heading

class Anti_Ragging(models.Model):
	Name = models.CharField(max_length=50)
	Designation = models.CharField(max_length=50)
	Contact_No = models.CharField(max_length=50)

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Name

class About_University(models.Model):
	Heading = models.CharField(max_length=50)
	Description = models.TextField(max_length=1000)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Heading

class Contact(models.Model):
	HEADING_CHOICES = (
        ('Address','Address'),
        ('Contact_No','Contact No.'),
        ('Email_Address','Email Address'),
        ('Hours','Working Hours'),
        ('Facebook','Facebook'),
        ('Linkedin','Linkedin'),
        ('Google+','Google+'),
        ('Twitter','Twitter'),
    )

	Heading = models.CharField(max_length=50,choices=HEADING_CHOICES, default='Address')
	Description = models.TextField(max_length=100)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Heading

'''
class Research_Cell(models.Model):
	pass

class Development_Center(models.Model):
	pass

class Publication(models.Model):
	pass
'''