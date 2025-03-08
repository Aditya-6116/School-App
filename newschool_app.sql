-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: school_app
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `marksxii2023`
--

DROP TABLE IF EXISTS `marksxii2023`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marksxii2023` (
  `Admission_No` int DEFAULT NULL,
  `Name` varchar(25) DEFAULT NULL,
  `Term_1` decimal(6,2) DEFAULT NULL,
  `Term_2` decimal(6,2) DEFAULT NULL,
  KEY `Admission_No` (`Admission_No`),
  CONSTRAINT `marksxii2023_ibfk_1` FOREIGN KEY (`Admission_No`) REFERENCES `student` (`Admission_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marksxii2023`
--

LOCK TABLES `marksxii2023` WRITE;
/*!40000 ALTER TABLE `marksxii2023` DISABLE KEYS */;
/*!40000 ALTER TABLE `marksxii2023` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Roll_No` int DEFAULT NULL,
  `Admission_No` int NOT NULL,
  `Name` varchar(25) DEFAULT NULL,
  `Class` varchar(5) DEFAULT NULL,
  `Physics` decimal(6,2) DEFAULT NULL,
  `Chemistry` decimal(6,2) DEFAULT NULL,
  `Maths` decimal(6,2) DEFAULT NULL,
  `Biology` decimal(6,2) DEFAULT NULL,
  `Computer` decimal(6,2) DEFAULT NULL,
  `English` decimal(6,2) DEFAULT NULL,
  `Accountancy` decimal(6,2) DEFAULT NULL,
  `Economics` decimal(6,2) DEFAULT NULL,
  `Info_Practices` decimal(6,2) DEFAULT NULL,
  `Business` decimal(6,2) DEFAULT NULL,
  `Bus` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`Admission_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (9,3578,'Mathew Jacob','XII A',99.97,89.62,55.14,79.05,NULL,63.27,NULL,NULL,NULL,NULL,'B'),(13,3770,'Sanchit Kumar','XII A',69.49,51.08,80.67,70.24,NULL,68.76,NULL,NULL,NULL,NULL,'B'),(14,3867,'Shreenanda V','XII A',55.26,82.38,90.13,73.35,NULL,78.53,NULL,NULL,NULL,NULL,'NO'),(3,3981,'Archana Kapoor','XII A',82.60,64.53,68.37,79.56,NULL,66.81,NULL,NULL,NULL,NULL,'NO'),(8,3991,'Karthikeya Rana','XII A',54.43,84.18,86.23,83.53,NULL,87.78,NULL,NULL,NULL,NULL,'NO'),(12,4088,'Krish Rajeev','XII B',94.40,59.47,60.63,NULL,53.29,81.15,NULL,NULL,NULL,NULL,'C'),(7,4101,'Harry Eastwood','XII B',96.17,77.38,63.66,NULL,86.94,98.83,NULL,NULL,NULL,NULL,'B'),(10,4123,'Grace Ann','XII C',NULL,NULL,NULL,NULL,NULL,86.74,63.27,65.72,53.80,60.50,'C'),(7,4166,'Jones Alias','XII A',66.80,90.46,68.58,53.47,NULL,56.87,NULL,NULL,NULL,NULL,'B'),(9,4252,'Finn Ryder','XII C',NULL,NULL,NULL,NULL,NULL,97.52,94.73,74.00,80.39,54.00,'B'),(13,4277,'Jack Daniel','XII C',NULL,NULL,NULL,NULL,NULL,80.32,81.90,89.42,83.97,71.89,'A'),(1,4361,'Aadhish K','XII B',94.13,73.60,90.59,NULL,82.03,77.00,NULL,NULL,NULL,NULL,'B'),(1,4513,'Aarti Sharma','XII A',58.17,50.22,81.30,83.75,NULL,51.92,NULL,NULL,NULL,NULL,'B'),(4,4609,'Ahmed Iqbal','XII B',66.70,98.75,57.39,NULL,54.07,71.63,NULL,NULL,NULL,NULL,'NO'),(4,4638,'Ashok Khanna','XII A',98.80,83.57,69.53,76.93,NULL,69.67,NULL,NULL,NULL,NULL,'B'),(12,4665,'Riya Sharma','XII A',76.64,59.72,59.61,50.79,NULL,95.32,NULL,NULL,NULL,NULL,'B'),(2,4677,'Abraham David','XII B',97.05,84.99,87.21,NULL,58.29,72.46,NULL,NULL,NULL,NULL,'NO'),(2,4737,'Bella Paul','XII C',NULL,NULL,NULL,NULL,NULL,94.21,99.01,51.56,60.49,87.11,'C'),(3,4768,'Aditya Birla','XII B',92.56,78.59,87.18,NULL,97.37,85.52,NULL,NULL,NULL,NULL,'B'),(10,4976,'Jennifer James','XII B',92.93,89.09,57.39,NULL,94.72,55.64,NULL,NULL,NULL,NULL,'B'),(15,5016,'Sonal Dutt','XII A',95.50,78.41,79.19,65.97,NULL,66.59,NULL,NULL,NULL,NULL,'B'),(9,5033,'Jayden Shawn','XII B',79.11,90.75,63.32,NULL,70.77,90.17,NULL,NULL,NULL,NULL,'C'),(15,5132,'Michael David ','XII B',69.26,91.34,94.70,NULL,94.44,81.93,NULL,NULL,NULL,NULL,'C'),(5,5147,'Christopher J','XII C',NULL,NULL,NULL,NULL,NULL,72.18,94.20,88.30,87.10,60.20,'B'),(14,5162,'Mandy Eaves','XII B',99.59,72.79,89.32,NULL,54.56,78.34,NULL,NULL,NULL,NULL,'NO'),(2,5177,'Anubhav Singh','XII A',60.39,60.96,83.41,61.69,NULL,83.96,NULL,NULL,NULL,NULL,'A'),(11,5207,'Kass Ann Mathew','XII B',63.83,64.95,99.42,NULL,58.85,58.63,NULL,NULL,NULL,NULL,'B'),(14,5225,'Jacob S','XII C',NULL,NULL,NULL,NULL,NULL,65.03,78.31,91.24,87.66,98.39,'A'),(17,5376,'Nirmal John','XII B',56.87,62.96,90.72,NULL,82.27,91.55,NULL,NULL,NULL,NULL,'B'),(5,5395,'Anoop Pathak','XII B',56.30,81.75,85.39,NULL,85.67,88.91,NULL,NULL,NULL,NULL,'B'),(1,5398,'Aisha Bin Ali','XII C',NULL,NULL,NULL,NULL,NULL,52.31,53.70,95.41,84.16,85.07,'B'),(11,5413,'Henry Samuel','XII C',NULL,NULL,NULL,NULL,NULL,75.62,87.58,88.93,92.11,75.45,'A'),(12,5428,'Isabelle Sam','XII C',NULL,NULL,NULL,NULL,NULL,69.34,75.96,81.14,56.47,72.14,'NO'),(8,5507,'Hritik Roshan','XII B',72.09,55.91,87.03,NULL,64.64,59.43,NULL,NULL,NULL,NULL,'NO'),(6,5546,'John Smith','XII A',57.97,77.97,97.89,71.18,NULL,87.05,NULL,NULL,NULL,NULL,'NO'),(11,5555,'Neha Ann','XII A',84.24,78.66,50.87,97.78,NULL,92.50,NULL,NULL,NULL,NULL,'NO'),(3,5699,'Benjamin F','XII C',NULL,NULL,NULL,NULL,NULL,97.43,61.40,74.81,93.43,97.43,'A'),(10,5932,'Maya Dev','XII A',59.77,84.10,76.75,88.59,NULL,91.34,NULL,NULL,NULL,NULL,'NO'),(6,5933,'Evaniya K','XII B',98.07,52.52,64.14,NULL,92.47,78.25,NULL,NULL,NULL,NULL,'A'),(13,5996,'Lincoln Sam','XII B',53.74,55.28,58.18,NULL,95.45,74.60,NULL,NULL,NULL,NULL,'B'),(16,6128,'Kayla Mathew','XII C',NULL,NULL,NULL,NULL,NULL,81.32,96.99,92.08,93.93,78.25,'NO'),(15,6155,'Jessica Biju','XII C',NULL,NULL,NULL,NULL,NULL,89.38,58.75,92.08,56.73,62.82,'A'),(6,6210,'Daisy Thomas','XII C',NULL,NULL,NULL,NULL,NULL,99.92,84.29,53.57,81.22,97.11,'A'),(4,6442,'Chloe Park','XII C',NULL,NULL,NULL,NULL,NULL,57.43,66.20,99.96,64.41,60.87,'A'),(20,6444,'Ram Kumar','XII B',93.81,99.77,68.71,NULL,84.12,50.51,NULL,NULL,NULL,NULL,'A'),(8,6526,'Ethan V K','XII C',NULL,NULL,NULL,NULL,NULL,78.98,89.90,85.92,57.86,99.91,'A'),(18,6667,'Nura Khan','XII B',56.40,81.17,52.84,NULL,59.83,75.27,NULL,NULL,NULL,NULL,'NO'),(7,6763,'Emma Rose','XII C',NULL,NULL,NULL,NULL,NULL,94.65,97.66,76.12,66.57,60.43,'A'),(16,6781,'Muhammed Sayed','XII B',57.29,97.17,55.04,NULL,98.27,94.59,NULL,NULL,NULL,NULL,'NO'),(5,6843,'Ganesh Vikram','XII A',70.50,83.93,70.83,70.52,NULL,85.54,NULL,NULL,NULL,NULL,'C');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `Reg_No` int NOT NULL,
  `Name` varchar(25) DEFAULT NULL,
  `Subject` varchar(15) DEFAULT NULL,
  `Class` varchar(8) DEFAULT NULL,
  `Bus` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`Reg_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (118,'Anjali Dev','Chemistry','XII A,B','C'),(129,'Arjun Prateek','Maths','XII A,B','C'),(140,'Roshini Manoj','Physics','XII A','C'),(154,'Devi Prasad','Business','XII C','C'),(168,'Uday Kumar','English','XII B','NO'),(183,'Neha Sharma','Computer','XII B','C'),(309,'Priya Arun','Economics','XII C','C'),(346,'Kaavya Jha','Physics','XII B','B'),(371,'Yuvraj Chauhan','English','XII A,C','A'),(378,'Tara Varma','Biology','XII A','C'),(384,'Prachi Verma','Accountancy','XII C','NO'),(449,'Varun Nair','Info Practices','XII A,C','NO');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-20 18:20:27
