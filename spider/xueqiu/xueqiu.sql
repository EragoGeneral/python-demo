/*
SQLyog Professional v12.08 (64 bit)
MySQL - 5.7.13-log : Database - xueqiu
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`xueqiu` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `xueqiu`;

/*Table structure for table `account` */

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Table structure for table `history` */

DROP TABLE IF EXISTS `history`;

CREATE TABLE `history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) DEFAULT NULL,
  `stock_symbol` varchar(16) DEFAULT NULL,
  `stock_name` varchar(16) DEFAULT NULL,
  `stock_id` int(11) DEFAULT NULL,
  `net_value` float DEFAULT NULL,
  `prev_net_value` float DEFAULT NULL,
  `prev_price` float DEFAULT NULL,
  `prev_target_volume` float DEFAULT NULL,
  `prev_target_weight` float DEFAULT NULL,
  `prev_volume` float DEFAULT NULL,
  `prev_weight` float DEFAULT NULL,
  `prev_weight_adjusted` float DEFAULT NULL,
  `price` float DEFAULT NULL,
  `proactive` int(11) DEFAULT NULL,
  `rebalancing_id` int(11) DEFAULT NULL,
  `target_volume` float DEFAULT NULL,
  `target_weight` float DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `volume` float DEFAULT NULL,
  `weight` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=857 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
