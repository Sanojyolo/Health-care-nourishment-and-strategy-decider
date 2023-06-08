-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Dec 25, 2022 at 07:24 AM
-- Server version: 10.1.19-MariaDB
-- PHP Version: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `healthcarenourishmentdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `fcm_attendance`
--

CREATE TABLE `fcm_attendance` (
  `atno` int(100) NOT NULL,
  `trainerid` varchar(100) DEFAULT NULL,
  `memberid` varchar(100) DEFAULT NULL,
  `membername` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `fcm_attendance`
--

INSERT INTO `fcm_attendance` (`atno`, `trainerid`, `memberid`, `membername`, `date`) VALUES
(1, '1', '6', '1', '2023-02-09'),
(2, '1', '6', '1', '2023-02-05');

-- --------------------------------------------------------

--
-- Table structure for table `fcm_datasets`
--

CREATE TABLE `fcm_datasets` (
  `no` int(100) NOT NULL,
  `memberno` varchar(100) DEFAULT NULL,
  `membername` varchar(100) DEFAULT NULL,
  `bmirange` varchar(100) DEFAULT NULL,
  `purpose` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `class` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `fcm_datasets`
--

INSERT INTO `fcm_datasets` (`no`, `memberno`, `membername`, `bmirange`, `purpose`, `category`, `class`, `date`) VALUES
(3, '1', 'm1', 'Normalweight', 'massincrease', 'highprotien', 'yes', '2023-01-07'),
(4, '2', 'm2', 'Normalweight', 'massincrease', 'highprotien', 'yes', '2023-01-07'),
(5, '3', 'm3', 'Normalweight', 'massincrease', 'highprotien', 'no', '2023-01-07'),
(6, '4', 'm4', 'Normalweight', 'massincrease', 'highprotien', 'yes', '2023-01-07'),
(7, '5', 'm5', 'Overweight', 'massincrease', 'highprotien', 'no', '2023-01-07'),
(8, '6', 'm6', 'Overweight', 'massincrease', 'highprotien', 'no', '2023-01-07'),
(9, '7', 'm7', 'Overweight', 'massincrease', 'nutral', 'yes', '2023-01-07'),
(10, '8', 'm8', 'Overweight', 'massincrease', 'nutral', 'yes', '2023-01-07'),
(11, '9', 'm9', 'Underweight', 'massincrease', 'highprotien', 'yes', '2023-01-07'),
(12, '10', 'm10', 'Underweight', 'massincrease', 'nutral', 'no', '2023-01-07'),
(13, '11', 'm11', 'Underweight', 'massincrease', 'highprotien', 'yes', '2023-01-07'),
(14, '12', 'm12', 'Normalweight', 'massdecrease', 'nutral', 'no', '2023-01-07'),
(15, '13', 'm13', 'Normalweight', 'massdecrease', 'lowcalory', 'yes', '2023-01-07'),
(16, '14', 'm14', 'Normalweight', 'massdecrease', 'lowcalory', 'yes', '2023-01-07'),
(17, '15', 'm15', 'Overweight', 'massdecrease', 'lowcalory', 'yes', '2023-01-07'),
(18, '16', 'm16', 'Overweight', 'massdecrease', 'nutral', 'no', '2023-01-07'),
(19, '17', 'm17', 'Overweight', 'massdecrease', 'lowcalory', 'yes', '2023-01-07'),
(20, '18', 'm18', 'Underweight', 'massdecrease', 'lowcalory', 'yes', '2023-01-07'),
(21, '19', 'm19', 'Underweight', 'massdecrease', 'lowcalory', 'yes', '2023-01-07'),
(22, '20', 'm20', 'Underweight', 'massdecrease', 'nutral', 'no', '2023-01-07'),
(23, '21', 'm21', 'Normalweight', 'fitness', 'nutral', 'yes', '2023-01-07'),
(24, '22', 'm22', 'Normalweight', 'fitness', 'nutral', 'yes', '2023-01-07'),
(25, '23', 'm23', 'Normalweight', 'fitness', 'highprotien', 'no', '2023-01-07'),
(26, '24', 'm24', 'Overweight', 'fitness', 'lowcalory', 'yes', '2023-01-07'),
(27, '25', 'm25', 'Overweight', 'fitness', 'lowcalory', 'yes', '2023-01-07'),
(28, '26', 'm26', 'Overweight', 'fitness', 'nutral', 'no', '2021-01-07'),
(29, '27', 'm27', 'Underweight', 'fitness', 'highprotien', 'yes', '2021-01-07'),
(30, '28', 'm28', 'Underweight', 'fitness', 'highprotien', 'yes', '2021-01-07'),
(31, '29', 'm29', 'Underweight', 'fitness', 'nutral', 'no', '2021-01-07'),
(32, '30', 'm30', 'Obesity', 'massincrease', 'lowcalory', 'yes', '2021-01-07'),
(33, '31', 'm31', 'Obesity', 'massincrease', 'lowcalory', 'yes', '2021-01-07'),
(34, '32', 'm32', 'Obesity', 'massincrease', 'nutral', 'no', '2021-01-07'),
(35, '33', 'm33', 'Obesity', 'massdecrease', 'lowcalory', 'yes', '2021-01-07'),
(36, '34', 'm34', 'Obesity', 'massdecrease', 'lowcalory', 'yes', '2021-01-07'),
(37, '35', 'm35', 'Obesity', 'massdecrease', 'nutral', 'no', '2021-01-07'),
(38, '36', 'm36', 'Obesity', 'fitness', 'lowcalory', 'yes', '2021-01-07'),
(39, '37', 'm37', 'Obesity', 'fitness', 'lowcalory', 'yes', '2021-01-07'),
(40, '38', 'm38', 'Obesity', 'fitness', 'nutral', 'yes', '2021-01-07');

-- --------------------------------------------------------

--
-- Table structure for table `fcm_dietplans`
--

CREATE TABLE `fcm_dietplans` (
  `dientno` int(100) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `imagename` varchar(50) DEFAULT NULL,
  `details` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'created'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `fcm_dietplans`
--

INSERT INTO `fcm_dietplans` (`dientno`, `name`, `category`, `imagename`, `details`, `date`, `status`) VALUES
(1, 'name1', 'lowcalory', 'name1.jpg', 'This is a low calory Program1', '2023-01-30', 'created'),
(2, 'name2', 'highprotien', 'name2.jpg', 'This is a high protien Program1', '2023-01-30', 'created'),
(3, 'name3', 'nutral', 'name3.jpg', 'This is a nutral Program1', '2023-01-30', 'created'),
(4, 'name4', 'lowcalory', 'name4.jpg', 'This is a low calory Program2', '2023-01-30', 'created'),
(5, 'name5', 'highprotien', 'name5.jpg', 'This is a high protien Program2', '2023-01-30', 'created'),
(6, 'name6', 'nutral', 'name6.jpg', 'This is a nutral Program2', '2023-01-30', 'created'),
(7, 'diet10', 'highprotien', 'name10.jpg', 'This is a nutral Program10', '2023-01-30', 'created'),
(9, 'diet11', 'highprotien', 'diet11.jpg', 'Diet11 Details', '2023-01-30', 'created');

-- --------------------------------------------------------

--
-- Table structure for table `fcm_features`
--

CREATE TABLE `fcm_features` (
  `fno` int(100) NOT NULL,
  `memberid` varchar(100) NOT NULL,
  `membername` varchar(100) DEFAULT NULL,
  `height` varchar(100) DEFAULT NULL,
  `weight` varchar(100) DEFAULT NULL,
  `purpose` varchar(100) DEFAULT NULL,
  `bmi` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `fcm_features`
--

INSERT INTO `fcm_features` (`fno`, `memberid`, `membername`, `height`, `weight`, `purpose`, `bmi`) VALUES
(1, '6', 'userName1', '172', '75', 'fitness', '25.35154137371552');

-- --------------------------------------------------------

--
-- Table structure for table `fcm_members`
--

CREATE TABLE `fcm_members` (
  `userid` int(10) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Mobile_Number` varchar(20) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Dob` varchar(20) DEFAULT NULL,
  `Email` varchar(20) DEFAULT NULL,
  `User_name` varchar(20) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'created'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `fcm_members`
--

INSERT INTO `fcm_members` (`userid`, `Name`, `Mobile_Number`, `Gender`, `Dob`, `Email`, `User_name`, `Password`, `status`) VALUES
(6, 'userName1', '1123456578', 'Male', '2020-11-11', 'user5@user5.com', 'user1', 'user1', 'created'),
(7, 'Name1', '1234567890', 'Male', '2021-01-29', 'd@d.com', 'user2', 'user2', 'created'),
(8, 'member5', '1234567890', 'Male', '1989-02-15', 'member5@member5.com', 'member5', 'member5', 'created'),
(10, 'user6', '1234567891', 'Male', '1896-02-15', 'user6@user6.com', 'user6', 'user6', 'created');

-- --------------------------------------------------------

--
-- Table structure for table `fcm_messages`
--

CREATE TABLE `fcm_messages` (
  `msgno` int(100) NOT NULL,
  `trainerid` varchar(100) DEFAULT NULL,
  `trainername` varchar(100) DEFAULT NULL,
  `memberid` varchar(100) DEFAULT NULL,
  `membername` varchar(100) DEFAULT NULL,
  `message` varchar(500) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `fcm_messages`
--

INSERT INTO `fcm_messages` (`msgno`, `trainerid`, `trainername`, `memberid`, `membername`, `message`, `date`) VALUES
(1, '1', 'tname', '6', 'userName1', 'asdfasdsdfsdfsdfs', '2023-01-30'),
(2, '1', 'tname', '6', 'userName1', 'sdfsdsdfsdfsdfsdfsdf', '2023-01-30'),
(3, '1', 'tname', '6', 'userName1', 'asdfasdf3', '2023-01-30');

-- --------------------------------------------------------

--
-- Table structure for table `fcm_trainer`
--

CREATE TABLE `fcm_trainer` (
  `userid` int(10) NOT NULL,
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
  `userids` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `fcm_trainer`
--

INSERT INTO `fcm_trainer` (`userid`, `Name`, `Mobile_Number`, `Gender`, `Dob`, `Email`, `experience`, `details`, `User_name`, `Password`, `status`, `userids`) VALUES
(1, 'tname', '1234567890', 'm', '1989-01-01', 'tn@tn.com', '12', 'details1', 'trainer1', 'trainer1', 'active', '1'),
(2, 'dfg', '12545345', 'Male', '2021-01-01', 'dfg@sdg.com', '23', NULL, 'adf', 'asdfgg', 'active', '2'),
(3, 'dfgdfg', '44', 'Male', '2021-01-01', 'gsdfgd@sef.com', '23', NULL, 'asdf', 'hfghfgh', 'active', '3');

-- --------------------------------------------------------

--
-- Table structure for table `membertrainerselection`
--

CREATE TABLE `membertrainerselection` (
  `mapno` int(100) NOT NULL,
  `trainerid` varchar(100) DEFAULT NULL,
  `memberid` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'created'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `membertrainerselection`
--

INSERT INTO `membertrainerselection` (`mapno`, `trainerid`, `memberid`, `date`, `status`) VALUES
(1, '1', '6', '2023-01-30', 'deleted'),
(2, '2', '6', '2023-01-30', 'deleted'),
(3, '3', '6', '2023-01-30', 'deleted'),
(4, '1', '6', '2023-01-30', 'deleted'),
(5, '2', '6', '2023-01-30', 'deleted'),
(6, '3', '6', '2023-01-30', 'deleted'),
(7, '1', '6', '2023-01-30', 'created');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fcm_attendance`
--
ALTER TABLE `fcm_attendance`
  ADD PRIMARY KEY (`atno`);

--
-- Indexes for table `fcm_datasets`
--
ALTER TABLE `fcm_datasets`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `fcm_dietplans`
--
ALTER TABLE `fcm_dietplans`
  ADD PRIMARY KEY (`dientno`);

--
-- Indexes for table `fcm_features`
--
ALTER TABLE `fcm_features`
  ADD PRIMARY KEY (`fno`,`memberid`);

--
-- Indexes for table `fcm_members`
--
ALTER TABLE `fcm_members`
  ADD PRIMARY KEY (`userid`),
  ADD UNIQUE KEY `NewIndex1` (`Name`,`Mobile_Number`,`Email`,`User_name`);

--
-- Indexes for table `fcm_messages`
--
ALTER TABLE `fcm_messages`
  ADD PRIMARY KEY (`msgno`);

--
-- Indexes for table `fcm_trainer`
--
ALTER TABLE `fcm_trainer`
  ADD PRIMARY KEY (`userid`),
  ADD UNIQUE KEY `NewIndex1` (`Name`,`Mobile_Number`,`Email`,`User_name`);

--
-- Indexes for table `membertrainerselection`
--
ALTER TABLE `membertrainerselection`
  ADD PRIMARY KEY (`mapno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fcm_attendance`
--
ALTER TABLE `fcm_attendance`
  MODIFY `atno` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `fcm_datasets`
--
ALTER TABLE `fcm_datasets`
  MODIFY `no` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
--
-- AUTO_INCREMENT for table `fcm_dietplans`
--
ALTER TABLE `fcm_dietplans`
  MODIFY `dientno` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `fcm_features`
--
ALTER TABLE `fcm_features`
  MODIFY `fno` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `fcm_members`
--
ALTER TABLE `fcm_members`
  MODIFY `userid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `fcm_messages`
--
ALTER TABLE `fcm_messages`
  MODIFY `msgno` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `fcm_trainer`
--
ALTER TABLE `fcm_trainer`
  MODIFY `userid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `membertrainerselection`
--
ALTER TABLE `membertrainerselection`
  MODIFY `mapno` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
