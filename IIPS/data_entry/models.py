from django.db import models
import random
import uuid
import string


# Create your models here.
class Generate_Transaction_ID(models.Model):
	Temp_Transaction_ID = models.CharField(max_length=20, blank=True, unique=True, default=uuid.uuid4)
	Student_Name = models.CharField(max_length=50)
	Student_Roll_Number = models.CharField(max_length=12)
	
	def __unicode__(self):  # Python 3: def __str__(self)
		return self.Student_Name

class User_Temp(models.Model):
	Temp_Transaction_ID=  models.CharField(max_length=20,null =False)#'This is a temporary transaction id of the user.',
	First_Name= models.CharField(max_length=20,null =False)
	Full_name = models.CharField(max_length=50,default=full_name())
	Last_Name =models.CharField(max_length=25,null =False)
	Father_Name =models.CharField(max_length=50)
	Mother_Name =models.CharField(max_length=50)
	Email =models.CharField(max_length=50)
	Type =models.CharField(max_length=50)
	DOB= models.DateField()
	Local_Address =models.CharField(max_length=200,null=True)
	Permanent_Address =models.CharField(max_length=200,null=True)
	Mobile_Number =models.CharField(max_length=15)
	Telephone_Number =models.CharField(max_length=200,null=True)
	Roll_Number =models.CharField(max_length=200,null=True)
	Enrollment_Number =models.CharField(max_length=200,null=True)
	Discipline =models.CharField(max_length=200)
	Post =models.CharField(max_length=200)
	Responsibility =models.CharField(max_length=200)
	Batch_ID =models.CharField(max_length=200,null=True)
	Course_ID =models.SmallIntegerField()

	def full_name(self):
		return self.First_Name + self.Last_Name
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Full_Name

	#def authenticate(self):
	#	if Temp_Transaction_ID in Generate_Transaction_ID:

	#PRIMARY KEY (`Temp_Transaction_ID`)

'''
CREATE TABLE IF NOT EXISTS `Student_Info` (
`User_ID` int(6) NOT NULL COMMENT 'This is the user_ID from User_Master table',
`Enrollment_Number` varchar(10) NOT NULL,
`Roll_Number` varchar(10) NOT NULL,
`Current_Course` varchar(15) NOT NULL,
`Current_Sem` tinyint(2) NOT NULL COMMENT 'This is the current semester in which the student is studying',
`Enrollment_Year` year(4) NOT NULL,
`Batch_ID` varchar(10) NOT NULL,
`Alternate_Email` varchar(30) NOT NULL,
`Last_Qualification` text NOT NULL COMMENT 'Higher secondary, graduate, post-graduate ,others',
`Institute Name` text NOT NULL COMMENT 'Name of the institute last attended',
`Univ_Board` text NOT NULL COMMENT 'The university or board of the institute last attended',
`Area_Of_Interest` mediumtext COMMENT 'Area of interest for student',
`Internship_Exp` smallint(3) DEFAULT NULL COMMENT 'Internship experience in months(if any)',
`Picture` varchar(40) DEFAULT NULL COMMENT 'Link of the picture of the student',
`Web_Link` varchar(50) DEFAULT NULL,
`Blog_Link` varchar(50) DEFAULT NULL,
`Github_Link` varchar(50) DEFAULT NULL,
`LinkedIn_Link` varchar(50) DEFAULT NULL,
`Facebook_Link` varchar(50) DEFAULT NULL,
`Googleplus_Link` varchar(50) DEFAULT NULL,
`Twitter_Link` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='This table includes basic info of each existing student in the system.';

'''