from django.db import models

# Create your models here.

class Course(models.Model):
	course_name = models.CharField(max_length=200)
	program_name = models.CharField(max_length=200)
	number_of_semester = models.PositiveSmallIntegerField(null=True)
	discipline = models.CharField(max_length=200,null=True) #computer or management
	description = models.CharField(max_length=1000,null=True)
	objective = models.CharField(max_length=1000,null=True)
	learning_outcomes = models.CharField(max_length=1000,null=True)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.course_name
	
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
		return self.first_name
	#PRIMARY KEY (`Temp_Transaction_ID`)
	

#Table structure for table `Staff_Info`
class Staff_Info(models.Model):
	User_ID=models.SmallIntegerField(max_length=6)
	Post=models.CharField(max_length=40)
	Responsibility=models.CharField(max_length=40)
	Web_Link=models.CharField(max_length=40,default=None)
	Blog_Link=models.CharField(max_length=40,default=None)
	Alternate_Email=models.CharField(max_length=40,default=None)
	Linkedin_Link=models.CharField(max_length=40,default=None)
	Facebook_Link=models.CharField(max_length=40,default=None)
	Googleplus_Link=models.CharField(max_length=40,default=None)
	Twitter_Link=models.CharField(max_length=40,default=None)
	Picture=models.CharField(max_length=40,default=None)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.User_ID

#Table structure for table `Faculty_Info`

class Faculty_Info(models.Model):
	User_ID=models.SmallIntegerField(max_length=6)#This is the user_id from User_master table.
	Discipline =models.CharField(max_length=200)
	Post=models.CharField(max_length=200)
	Responsibility=models.CharField(max_length=200)
	DOJ=models.DateField() 		#Date of Joining
	Area_Of_Interest=models.CharField(max_length=200)
	Previous_Job=models.CharField(max_length=200)
	Web_Link=models.CharField(max_length=40,default=None)
	Blog_Link=models.CharField(max_length=40,default=None)
	Alternate_Email=models.CharField(max_length=40,default=None)
	Linkedin_Link=models.CharField(max_length=40,default=None)
	Facebook_Link=models.CharField(max_length=40,default=None)
	Googleplus_Link=models.CharField(max_length=40,default=None)
	Twitter_Link=models.CharField(max_length=40,default=None)
	Picture=models.CharField(max_length=40,default=None)
	Resume =models.CharField(max_length=40,default=None)#Link to resume
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.User_ID
	#PRIMARY KEY (`Pitcture`)


#Table structure for Admission Module

class Entrance_Exam_CET(models.Model):
	CET = models.CharField(max_length=1000,default=None)
	List_Of_Criteria_For_Admission = models.CharField(max_length=1000,default=None)
	Admission_Process_In_Affiliated_Colleges_If_Department_Is_Monitoring= models.CharField(max_length=1000,default=None)
	Student_Profile_Analysis = models.CharField(max_length=1000,default=None)
	Admission_To_NRI_PIO = models.CharField(max_length=1000,default=None)
	Entrance_Test = models.CharField(max_length=1000,default=None)
	Reservation_Policy_Conversion_Of_Seats=models.CharField(max_length=1000,default=None)
	Councling=models.ForeignKey('Councling')
	Eligiblity=models.ForeignKey('Eligiblity')
	Refund_Of_Fee=models.CharField(max_length=1000,default=None)
	Other_Important_points=models.CharField(max_length=1000,default=None)
	Hostel_Accomodation=models.CharField(max_length=1000,default=None)
	Note=models.CharField(max_length=1000,default=None)
	
class Eligiblity(models.Model):
	Minimum_Percentage_For_Admissions_Eligibility_or_Appearing_In_Entrance_Test=models.CharField(max_length=1000,default=None)
	Age_Limit = models.CharField(max_length=1000,default=None)
	Non_Eligiblity_For_Admission=models.CharField(max_length=1000,default=None)

class Councling(models.Model):
	description=models.CharField(max_length=1000,default=None)

class How_T0_Apply(models.Model):
	description=models.CharField(max_length=1000,default=None)

class Fee_Structure(models.Model):
	course=models.CharField(max_length=40),primary_key=True)
	School_Of_Studies=models.CharField(max_length=60)
	Group=models.CharField(max_length=1)
	Fees_Excluding_Student_Services_Fee=models.PositiveSmallIntegerField()
	Caution_Money_Refundable=models.PositiveSmallIntegerField()

#Table structure for table Sylabus

class Syllabus(models.Model):
	Semester=models.PositiveSmallIntegerField()
	Subject=models.ForeignKey('Subject')

class Subject(models.Model):
	Subject=models.CharField(max_length=40,primary_key=True)
	Subject_ID=models.CharField(max_length=10)
	Aim_Of_course=models.CharField(max_length=400)
	Objective=models.CharField(max_length=400)
	Course_Content=models.ForeignKey('Course_Content')

class Course_Content(models.Model):
	Unit=models.PositiveSmallIntegerField()
	Contents=models.CharField(max_length=400)
	


'''

-- --------------------------------------------------------
-- 
-- Table structure for table `Course_Info`
--
CREATE TABLE IF NOT EXISTS `Course_Info` (
`Course_ID` tinyint(2) NOT NULL AUTO_INCREMENT COMMENT 'Unique course Id for each course',
`Course_Name` varchar(15) NOT NULL,
`Number_Of_Semester` tinyint(2) NOT NULL COMMENT 'Total number of semester in a course',
`Discipline` text NOT NULL COMMENT 'The discipline (computer or management)',
PRIMARY KEY (`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='This table includes basic info of each course in the institute.' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------
-- 
-- Table structure for table `Staff_Info`
-- 
CREATE TABLE IF NOT EXISTS `Staff_Info` (
`User_ID` int(6) NOT NULL,
`Post` text NOT NULL,
`Responsibility` text,
`Web_Link` varchar(40) DEFAULT NULL,
`Blog_Link` varchar(40) DEFAULT NULL,
`Alternate_Email` varchar(40) DEFAULT NULL,
`Linkedin_Link` varchar(40) DEFAULT NULL,
`Facebook_Link` varchar(40) DEFAULT NULL,
`Googleplus_Link` varchar(40) DEFAULT NULL,
`Twitter_Link` varchar(40) DEFAULT NULL,
`Picture` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='This table includes basic information about staff.';

-- --------------------------------------------------------

-- --------------------------------------------------------
-- 
-- Table structure for table `Faculty_Info`
-- 
CREATE TABLE IF NOT EXISTS `Faculty_Info` (
`User_ID` int(6) NOT NULL COMMENT 'This is the user_id from User_master table.',
`Discipline` text NOT NULL,
`Post` text NOT NULL,
`Responsibility` text NOT NULL,
`DOJ` date NOT NULL COMMENT 'Date of Joining',
`Area_Of_Interest` text,
`Previous_Job` longtext,
`Alternate_Email` varchar(40) NOT NULL,
`Web_Link` varchar(40) DEFAULT NULL,
`Blog_Link` varchar(40) DEFAULT NULL,
`LinkedIn_Link` varchar(40) DEFAULT NULL,
`Facebook_Link` varchar(40) DEFAULT NULL,
`Googleplus_Link` varchar(40) DEFAULT NULL,
`Twitter_Link` varchar(40) DEFAULT NULL,
`Pitcture` varchar(11) NOT NULL COMMENT 'Link of the Picture',
`Resume` varchar(40) DEFAULT NULL COMMENT 'Link to resume',
PRIMARY KEY (`Pitcture`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='This table includes basic info of each faculty, in the system.';

-- 
-- Table structure for table `User_Temp`
-- 
CREATE TABLE IF NOT EXISTS `User_Temp` (
`Temp_Transaction_ID` varchar(10) NOT NULL COMMENT 'This is a temporary transaction id of the user.',
`First_Name` text NOT NULL,
`Last_Name` text NOT NULL,
`Father_Name` text,
`Mother_Name` text,
`Email` varchar(40) NOT NULL,
`Type` text NOT NULL,
`DOB` date DEFAULT NULL,
`Local_Address` varchar(40) DEFAULT NULL,
`Permanent_Address` varchar(40) DEFAULT NULL,
`Mobile_Number` varchar(14) NOT NULL,
`Telephone_Number` varchar(16) DEFAULT NULL,
`Roll_Number` varchar(10) DEFAULT NULL,
`Enrollment_Number` varchar(10) DEFAULT NULL,
`Discipline` text,
`Post` text,
`Responsibility` text,
`Batch_ID` varchar(8) DEFAULT NULL,
`Course_ID` tinyint(2) DEFAULT NULL,
PRIMARY KEY (`Temp_Transaction_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

'''