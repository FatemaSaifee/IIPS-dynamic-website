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