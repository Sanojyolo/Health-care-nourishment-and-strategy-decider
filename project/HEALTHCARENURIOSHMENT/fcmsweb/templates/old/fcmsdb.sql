/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.36-log : Database - fcmsdb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`fcmsdb` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `fcmsdb`;

/*Table structure for table `fcm_dietplans` */

DROP TABLE IF EXISTS `fcm_dietplans`;

CREATE TABLE `fcm_dietplans` (
  `dientno` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `details` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'created',
  PRIMARY KEY (`dientno`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `fcm_dietplans` */

insert  into `fcm_dietplans`(`dientno`,`name`,`category`,`details`,`date`,`status`) values (1,'name1','lowprotien','adkfadmnb\r\nhsdfjkasdjkf\r\ndbhfkasdfjk\r\ndnfjksdfjk\r\ndsfjksdhfk\r\n','2021-01-30','deleted'),(2,'name2','highprotien','sdfhjkdsfahndfdjkf\r\njnasdfkasdjk\r\nhndsjkfhjksdf\r\ndnfjsdhkf\r\nsdjfjksdfk\r\njsdfjkasdjko','2021-01-30','created');

/*Table structure for table `fcm_members` */

DROP TABLE IF EXISTS `fcm_members`;

CREATE TABLE `fcm_members` (
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

/*Data for the table `fcm_members` */

insert  into `fcm_members`(`userid`,`Name`,`Mobile_Number`,`Gender`,`Dob`,`Email`,`User_name`,`Password`,`status`) values (1,'employee1name','1234567801','male','1989-01-01','employee1@gmail.com1','user1','user1','active'),(2,'employee2name','1234567803','male','1989-01-01','employee2@gmail.com','user2','user2','active'),(3,'employee4','1212124354','male','2020-04-09','af@sdf.com','employee4','employee4','deleted'),(4,'username4','112345677890','FeMale','2020-11-11','user4@user4.com','user4','user4','active'),(6,'user5','1123456578','Male','2020-11-11','user5@user5.com','user5','user5','created'),(7,'Name1','1234567890','Male','2021-01-29','d@d.com','asdf','fgh','created');

/*Table structure for table `fcm_trainer` */

DROP TABLE IF EXISTS `fcm_trainer`;

CREATE TABLE `fcm_trainer` (
  `userid` int(10) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) DEFAULT NULL,
  `Mobile_Number` varchar(20) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Dob` varchar(20) DEFAULT NULL,
  `Email` varchar(20) DEFAULT NULL,
  `experience` varchar(20) DEFAULT NULL,
  `details` varchar(500) DEFAULT NULL,
  `User_name` varchar(20) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'created',
  PRIMARY KEY (`userid`),
  UNIQUE KEY `NewIndex1` (`Name`,`Mobile_Number`,`Email`,`User_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `fcm_trainer` */

insert  into `fcm_trainer`(`userid`,`Name`,`Mobile_Number`,`Gender`,`Dob`,`Email`,`experience`,`details`,`User_name`,`Password`,`status`) values (1,'tname','1234567890','m','1989-01-01','tn@tn.com',NULL,NULL,'trainer1','trainer1','active'),(2,'dfg','12545345','Male','2021-01-01','dfg@sdg.com','23',NULL,'adf','asdfgg','active'),(3,'dfgdfg','44','Male','2021-01-01','gsdfgd@sef.com','23',NULL,'asdf','hfghfgh','active'),(4,'asdf','1234567890','Male','2021-01-08','f@h.com','12','dsfaadsfasdfsdfd','trainer5','password5','created');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
