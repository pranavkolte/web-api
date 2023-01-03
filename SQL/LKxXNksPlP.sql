-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 04, 2022 at 08:09 AM
-- Server version: 8.0.13-4
-- PHP Version: 7.2.24-0ubuntu0.18.04.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `LKxXNksPlP`
--

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `ID` int(11) NOT NULL,
  `username` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `status` int(1) NOT NULL DEFAULT '0',
  `IP` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `last_access` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`ID`, `username`, `password`, `status`, `IP`) VALUES
(1, 'user', '8D969EEF6ECAD3C29A3A629280E686CF0C3F5D5A86AFF3CA12020C923ADC6C92', 0, '192.168.145.25');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `ID` int(11) NOT NULL,
  `name` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `gender` varchar(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `age` int(11) NOT NULL,
  `mobile` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `medical_history` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `last_update` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`ID`, `name`, `gender`, `age`, `mobile`, `address`, `medical_history`) VALUES
(1, 'new goju', 'male', 24, '9638527410', '420 powder gali', 'sickkkk'),
(2, 'Gojou Satori', 'male', 24, '9638527410', '420 powder gali', 'sickkkk'),
(3, 'Gojou Satori', 'male', 24, '9638527410', '420 powder gali', 'sickkkk'),
(4, 'lavieee', 'male', 24, '9876543210', 'eldian empire', 'not so sick'),
(5, 'Levi Akeraman', 'male', 24, '9876543210', 'eldian empire', 'not so sick'),
(6, 'Levi Akeraman', 'male', 24, '9876543210', 'eldian empire', 'not so sick'),
(7, 'new eren', 'male', 24, '9876543210', 'eldian empire', 'not so sick'),
(8, 'Might Guy', 'male', 24, '9876543210', 'eldian empire', 'not soso sick'),
(9, 'Might Guy', 'male', 24, '9876543210', 'eldian empire', 'not soso sick'),
(12, 'rockkkk', 'male', 45, '8975641230', 'konohamaru', 'fuckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'),
(13, 'Naruto Uzumaki', 'male', 24, '9876543210', 'eldian empire', 'not soso sick'),
(14, 'Naruto Uzumaki', 'male', 24, '9876543210', 'Leaf Village', 'being dumb'),
(15, 'hinata ', 'female', 20, '9638521470', 'leaf village', 'seriously adorable'),
(16, 'haruno sakura', 'female', 20, '95135746280', 'leaf village near hokage office fuckkkkkkk', 'so dumb'),
(17, 'Shikimaru', 'male', 20, '9865327410', 'soooooooooooooooooooooooo dontttttttttt know', 'colllllllllllllllllllllllllllllllllllllllloooooooooo'),
(18, 'Jiraya Galant', 'male', 55, '897564132', 'leaf village ', 'lsot mind'),
(19, 'Obita Uchiha', 'male', 25, '7654981203', 'kono ha village ', 'lost one eye'),
(20, 'tanjiro', 'male', 18, '897546321', 'dont know yet', 'none '),
(21, 'ok ', 'male', 65, '654987321', 'kjhzdv', 'jkjdhfcdj'),
(22, 'kokko', 'female', 65, '654321987', 'kokoko', 'kolooloo');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
