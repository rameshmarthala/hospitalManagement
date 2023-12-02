/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - block_chain
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`block_chain` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `block_chain`;

/*Table structure for table `bookslot` */

DROP TABLE IF EXISTS `bookslot`;

CREATE TABLE `bookslot` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `dname` varchar(100) DEFAULT NULL,
  `pname` varchar(100) DEFAULT NULL,
  `demail` varchar(100) DEFAULT NULL,
  `pemail` varchar(100) DEFAULT NULL,
  `sym` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `dtype` varchar(100) DEFAULT NULL,
  `dno` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  `action` varchar(100) DEFAULT 'waiting',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `bookslot` */

insert  into `bookslot`(`id`,`dname`,`pname`,`demail`,`pemail`,`sym`,`age`,`dtype`,`dno`,`date`,`status`,`action`) values (1,'Lakshmi','Keerthana','lakshmi@gmail.com','cse.takeoff@gmail.com','Heartburn pain','26','Cardiologist','5678909876','2021-06-12','Completed','Success');

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `dtype` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  `gen` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`id`,`name`,`dtype`,`email`,`pwd`,`dob`,`addr`,`pno`,`gen`) values (1,'lakshmi','Cardiologist','lakshmi@gmail.com','1','2021-06-06','ongole','5678909876','female');

/*Table structure for table `patient` */

DROP TABLE IF EXISTS `patient`;

CREATE TABLE `patient` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `gen` varchar(100) DEFAULT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `pno` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `patient` */

insert  into `patient`(`id`,`name`,`email`,`pwd`,`gen`,`addr`,`dob`,`pno`) values (1,'keerthana','cse.takeoff@gmail.com','1','ms','tirupati','2021-06-09','1234567890');

/*Table structure for table `reports` */

DROP TABLE IF EXISTS `reports`;

CREATE TABLE `reports` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `fid` int(10) DEFAULT NULL,
  `block1` longblob,
  `block2` longblob,
  `hash1` varchar(200) DEFAULT NULL,
  `hash2` varchar(200) DEFAULT NULL,
  `pname` varchar(100) DEFAULT NULL,
  `pemail` varchar(100) DEFAULT NULL,
  `sym` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `reports` */

insert  into `reports`(`id`,`fid`,`block1`,`block2`,`hash1`,`hash2`,`pname`,`pemail`,`sym`,`date`) values (3,1,'Daily lots of data is exchanged and loaded on a cloud into\ndifferent sectors one of which is the health sector. Data\nexchanged between the patient and doctors need to be\nsecured to gain patients\' trust. Blockchain is a mechanism\ninvented to secure data in a more advanced way. Blockchain\nstores data into chunks that make it hard to decode, which\nwill help provide an extr','Daily lots of data is exchanged and loaded on a cloud into\ndifferent sectors one of which is the health sector. Data\nexchanged between the patient and doctors need to be\nsecured to gain patients\' trust. Blockchain is a mechanism\ninvented to secure data in a more advanced way. Blockchain\nstores data into chunks that make it hard to decode, which\nwill help provide an extra layer of security. Hash chain is the\nmost reliable part of the blockchain that will help keep the\ndata unreadable. This data can be secured by using a\nblockchain mechanism at the backend of any hospital\nwebsite to store the reports of the patients and maintain a\ntwo-way authentication for doctorâ€™s access to the reports.\nUsing the concepts of dividing data into chunks and\nestablishing an inter-link between each chunk is one of the\naspects of blockchain which is implemented on the hospital\ngenerated data to inherit blockchain mechanism. In this\npaper, we have discussed the benefits of using this\nmechanism to secure patients\' reports and how it increases\ntrust in the stored data.\nKeywords: - Blockchain, Cloud, Healthcare, Security, AES','9a611ae3732b13d72ae219f89459089819a87580','37fecf3e19620e14a9fe45a3f763a3077efb6835','Keerthana','cse.takeoff@gmail.com','Heartburn pain','2021-06-11 10:44:16.746990');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
