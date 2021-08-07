-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 27, 2021 at 06:34 AM
-- Server version: 5.6.51-log
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test1`
--

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
CREATE TABLE IF NOT EXISTS `test` (
  `name` varchar(50) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `pincode` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `district` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `commentbox` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`name`, `Gender`, `pincode`, `address`, `city`, `district`, `type`, `commentbox`) VALUES
('A', 'Male', '24242', 'dsadfsa', 'dfs', 'sds', NULL, '.!notebook.!frame.!frame.!frame3.!frame.!text'),
('Ajay ', '', '111111', '1-2-323-3Street', 'Ned', 'MH', NULL, '\n'),
('Aj', 'Male', '11111', '1-12-1-212street', 'Ned', 'MH', NULL, 'test\n'),
('Aj', 'Male', '2555', 'baba Nagar Nanded', 'Ned', 'MH', NULL, 'There is No Suggestion From My Side\n'),
('Aj', 'Male', '123456', '1-2-3---street', 'NA', 'NA', NULL, 'testing \n'),
('test', 'Male', 'test', 'test', 'test', 'v', 'Tansport', 'test\n'),
('test', 'Male', 'test', 'test', 'test', 'test', 'test\n', 'TansportWaterElectricityRoadServiceHospitalsTaxCommunicationEducationDrainageGas issueOther'),
('test', 'Male', 'test', 'test', 'test', 'test', 'test\n', 'TansportWaterElectricityRoadServiceHospitalsTaxCommunicationEducationDrainageGas issueOther'),
('datacheck', 'Male', 'datacheck', 'datacheck', 'datacheck', 'datacheck', 'TansportWaterElectricity', 'datacheck\n'),
('Aj', 'Male', '1234', 'aa', 'aaa', 'aaaa', 'Tansport,Water', 'aaaaaaaa\n'),
('Santosh', 'Male', '12345', 'Kabra nagar ', 'Ned', 'MH', 'Other', 'just checking\n'),
('Aj', 'Male', '245shghsnvhjhj', 'dghs', 'svhs', 'nff', 'Tansport', 'test\n');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
