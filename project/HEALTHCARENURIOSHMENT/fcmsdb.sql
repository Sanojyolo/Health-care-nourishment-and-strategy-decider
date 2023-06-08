/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.36-log : Database - pdmsdb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`pdmsdb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `pdmsdb`;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedbackid` int(20) NOT NULL AUTO_INCREMENT,
  `raisedid` varchar(50) DEFAULT NULL,
  `raisedname` varchar(100) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `details` varchar(500) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`feedbackid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `feedback` */

insert  into `feedback`(`feedbackid`,`raisedid`,`raisedname`,`feedback`,`details`,`date`) values (1,'1','user1','feedback1','feedback1details','2020-11-18'),(2,'1','user1','feedback2','feedback2details','2020-11-18');

/*Table structure for table `files` */

DROP TABLE IF EXISTS `files`;

CREATE TABLE `files` (
  `fileid` int(55) NOT NULL AUTO_INCREMENT,
  `uploaderid` varchar(55) DEFAULT NULL,
  `uploadername` varchar(55) DEFAULT NULL,
  `filename` varchar(55) DEFAULT NULL,
  `filedesc` varchar(55) DEFAULT NULL,
  `status` varchar(55) DEFAULT 'active',
  UNIQUE KEY `id` (`fileid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `files` */

insert  into `files`(`fileid`,`uploaderid`,`uploadername`,`filename`,`filedesc`,`status`) values (1,'1','user1','file1','file1des','deleted'),(2,'1','user1','file2','filedesc','deleted'),(3,'1','user1','file5','file5desc','active'),(4,'1','user1','file6','file6desc','active');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `requestid` int(55) NOT NULL AUTO_INCREMENT,
  `uploaderid` varchar(55) DEFAULT NULL,
  `uploadername` varchar(55) DEFAULT NULL,
  `filename` varchar(55) DEFAULT NULL,
  `filedesc` varchar(55) DEFAULT NULL,
  `status` varchar(55) DEFAULT 'created',
  `raisingdate` varchar(35) DEFAULT NULL,
  `approveddate` varchar(35) DEFAULT NULL,
  UNIQUE KEY `id` (`requestid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`requestid`,`uploaderid`,`uploadername`,`filename`,`filedesc`,`status`,`raisingdate`,`approveddate`) values (1,'1','user1','file5','file5desc','approved','2020-11-11',NULL),(2,'1','user1','file6','file6desc','approved','2020-11-11','2020-11-18');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `userid` int(10) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) DEFAULT NULL,
  `Mobile_Number` varchar(20) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Dob` varchar(20) DEFAULT NULL,
  `Email` varchar(20) DEFAULT NULL,
  `User_name` varchar(20) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'created',
  PRIMARY KEY (`userid`),
  UNIQUE KEY `NewIndex1` (`Name`,`Mobile_Number`,`Email`,`User_name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `user` */

insert  into `user`(`userid`,`Name`,`Mobile_Number`,`Gender`,`Dob`,`Email`,`User_name`,`Password`,`status`) values (1,'employee1name','1234567801','male','1989-01-01','employee1@gmail.com1','user1','user1','active'),(2,'employee2name','1234567803','male','1989-01-01','employee2@gmail.com','user2','user2','active'),(3,'employee4','1212124354','male','2020-04-09','af@sdf.com','employee4','employee4','deleted'),(4,'username4','112345677890','FeMale','2020-11-11','user4@user4.com','user4','user4','active'),(6,'user5','1123456578','Male','2020-11-11','user5@user5.com','user5','user5','created');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
