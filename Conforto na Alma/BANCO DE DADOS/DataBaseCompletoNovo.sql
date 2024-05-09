-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: conforto_na_alma
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agendamento_consulta`
--

DROP TABLE IF EXISTS `agendamento_consulta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agendamento_consulta` (
  `ID_AGENDAMENTO_CONSULTA` int NOT NULL AUTO_INCREMENT,
  `ID_CLIENTE` int DEFAULT NULL,
  `ID_MEDICO` int DEFAULT NULL,
  `TIPO_CONSULTA` varchar(100) DEFAULT NULL,
  `DATA_AGENDADA` date DEFAULT NULL,
  `DATA_AGENDAMENTO` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `HORARIO_CONSULTA` time DEFAULT NULL,
  `UNIDADE` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_AGENDAMENTO_CONSULTA`),
  KEY `ID_CLIENTE` (`ID_CLIENTE`),
  KEY `ID_MEDICO` (`ID_MEDICO`),
  CONSTRAINT `agendamento_consulta_ibfk_1` FOREIGN KEY (`ID_CLIENTE`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `agendamento_consulta_ibfk_2` FOREIGN KEY (`ID_MEDICO`) REFERENCES `medico` (`id_medico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agendamento_consulta`
--

LOCK TABLES `agendamento_consulta` WRITE;
/*!40000 ALTER TABLE `agendamento_consulta` DISABLE KEYS */;
/*!40000 ALTER TABLE `agendamento_consulta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `agendamento_exame`
--

DROP TABLE IF EXISTS `agendamento_exame`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agendamento_exame` (
  `ID_AGENDAMENTO_EXAME` int NOT NULL AUTO_INCREMENT,
  `ID_CLIENTE` int DEFAULT NULL,
  `ID_MEDICO` int DEFAULT NULL,
  `TIPO_EXAME` varchar(100) DEFAULT NULL,
  `DATA_AGENDADA` date DEFAULT NULL,
  `DATA_AGENDAMENTO` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `HORARIO_CONSULTA` time DEFAULT NULL,
  `UNIDADE` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_AGENDAMENTO_EXAME`),
  KEY `ID_CLIENTE` (`ID_CLIENTE`),
  KEY `ID_MEDICO` (`ID_MEDICO`),
  CONSTRAINT `agendamento_exame_ibfk_1` FOREIGN KEY (`ID_CLIENTE`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `agendamento_exame_ibfk_2` FOREIGN KEY (`ID_MEDICO`) REFERENCES `medico` (`id_medico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agendamento_exame`
--

LOCK TABLES `agendamento_exame` WRITE;
/*!40000 ALTER TABLE `agendamento_exame` DISABLE KEYS */;
/*!40000 ALTER TABLE `agendamento_exame` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `data_de_nascimento` date DEFAULT NULL,
  `rg` varchar(20) DEFAULT NULL,
  `cpf` varchar(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `cep` int DEFAULT NULL,
  `estado` varchar(100) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `bairro` varchar(100) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `numero` int DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  `genero` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE KEY `rg` (`rg`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `telefone` (`telefone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `id_funcionario` int NOT NULL AUTO_INCREMENT,
  `nome_funcionario` varchar(255) DEFAULT NULL,
  `data_de_nascimento` date DEFAULT NULL,
  `unidade` varchar(255) DEFAULT NULL,
  `rg` varchar(20) DEFAULT NULL,
  `cpf` varchar(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `cep` int DEFAULT NULL,
  `estado` varchar(100) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `bairro` varchar(100) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `numero` int DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  `genero` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_funcionario`),
  UNIQUE KEY `rg` (`rg`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medico`
--

DROP TABLE IF EXISTS `medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medico` (
  `id_medico` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `data_de_nascimento` date DEFAULT NULL,
  `crm` varchar(20) DEFAULT NULL,
  `unidade` varchar(255) DEFAULT NULL,
  `rg` varchar(20) DEFAULT NULL,
  `cpf` varchar(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `cep` int DEFAULT NULL,
  `estado` varchar(100) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `bairro` varchar(100) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `numero` int DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  `genero` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_medico`),
  UNIQUE KEY `crm` (`crm`),
  UNIQUE KEY `unidade` (`unidade`),
  UNIQUE KEY `rg` (`rg`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `telefone` (`telefone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medico`
--

LOCK TABLES `medico` WRITE;
/*!40000 ALTER TABLE `medico` DISABLE KEYS */;
/*!40000 ALTER TABLE `medico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receitas`
--

DROP TABLE IF EXISTS `receitas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receitas` (
  `ID_RECEITA` int NOT NULL AUTO_INCREMENT,
  `ID_CLIENTE` int DEFAULT NULL,
  `ID_MEDICO` int DEFAULT NULL,
  `ID_AGENDAMENTO_CONSULTA` int DEFAULT NULL,
  `RECEITA` text,
  PRIMARY KEY (`ID_RECEITA`),
  KEY `ID_CLIENTE` (`ID_CLIENTE`),
  KEY `ID_MEDICO` (`ID_MEDICO`),
  KEY `ID_AGENDAMENTO_CONSULTA` (`ID_AGENDAMENTO_CONSULTA`),
  CONSTRAINT `receitas_ibfk_1` FOREIGN KEY (`ID_CLIENTE`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `receitas_ibfk_2` FOREIGN KEY (`ID_MEDICO`) REFERENCES `medico` (`id_medico`),
  CONSTRAINT `receitas_ibfk_3` FOREIGN KEY (`ID_AGENDAMENTO_CONSULTA`) REFERENCES `agendamento_consulta` (`ID_AGENDAMENTO_CONSULTA`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receitas`
--

LOCK TABLES `receitas` WRITE;
/*!40000 ALTER TABLE `receitas` DISABLE KEYS */;
/*!40000 ALTER TABLE `receitas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resultados`
--

DROP TABLE IF EXISTS `resultados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resultados` (
  `ID_EXAME` int NOT NULL AUTO_INCREMENT,
  `ID_CLIENTE` int DEFAULT NULL,
  `ID_MEDICO` int DEFAULT NULL,
  `ID_AGENDAMENTO_EXAMES` int DEFAULT NULL,
  `RESULTADO` text,
  PRIMARY KEY (`ID_EXAME`),
  KEY `ID_CLIENTE` (`ID_CLIENTE`),
  KEY `ID_MEDICO` (`ID_MEDICO`),
  KEY `ID_AGENDAMENTO_EXAMES` (`ID_AGENDAMENTO_EXAMES`),
  CONSTRAINT `resultados_ibfk_1` FOREIGN KEY (`ID_CLIENTE`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `resultados_ibfk_2` FOREIGN KEY (`ID_MEDICO`) REFERENCES `medico` (`id_medico`),
  CONSTRAINT `resultados_ibfk_3` FOREIGN KEY (`ID_AGENDAMENTO_EXAMES`) REFERENCES `agendamento_exame` (`ID_AGENDAMENTO_EXAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resultados`
--

LOCK TABLES `resultados` WRITE;
/*!40000 ALTER TABLE `resultados` DISABLE KEYS */;
/*!40000 ALTER TABLE `resultados` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-08 21:07:40
