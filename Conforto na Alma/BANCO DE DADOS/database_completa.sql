-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: conforto_na_alma
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `atendimento`
--

DROP TABLE IF EXISTS `atendimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `atendimento` (
  `id_atendimento` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int DEFAULT NULL,
  `id_medico` int DEFAULT NULL,
  `data_agendamento` datetime DEFAULT NULL,
  `data_agendada` datetime DEFAULT NULL,
  `horario_consulta` varchar(100) DEFAULT NULL,
  `prescricao` text,
  `resultado` int DEFAULT NULL,
  `id_especialidade` int DEFAULT NULL,
  `id_tipo` int DEFAULT NULL,
  PRIMARY KEY (`id_atendimento`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_medico` (`id_medico`),
  KEY `id_especialidade` (`id_especialidade`),
  KEY `id_tipo` (`id_tipo`),
  CONSTRAINT `atendimento_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`),
  CONSTRAINT `atendimento_ibfk_2` FOREIGN KEY (`id_medico`) REFERENCES `medico` (`id_medico`),
  CONSTRAINT `atendimento_ibfk_3` FOREIGN KEY (`id_especialidade`) REFERENCES `especialidades` (`id_especialidade`),
  CONSTRAINT `atendimento_ibfk_4` FOREIGN KEY (`id_tipo`) REFERENCES `tipo_atendimento` (`id_tipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atendimento`
--

LOCK TABLES `atendimento` WRITE;
/*!40000 ALTER TABLE `atendimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `atendimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargo`
--

DROP TABLE IF EXISTS `cargo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cargo` (
  `id_cargo` int NOT NULL AUTO_INCREMENT,
  `cargo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_cargo`),
  UNIQUE KEY `cargo` (`cargo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargo`
--

LOCK TABLES `cargo` WRITE;
/*!40000 ALTER TABLE `cargo` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
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
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `especialidades`
--

DROP TABLE IF EXISTS `especialidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especialidades` (
  `id_especialidade` int NOT NULL AUTO_INCREMENT,
  `nome_da_especialidade` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_especialidade`),
  UNIQUE KEY `nome_da_especialidade` (`nome_da_especialidade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especialidades`
--

LOCK TABLES `especialidades` WRITE;
/*!40000 ALTER TABLE `especialidades` DISABLE KEYS */;
/*!40000 ALTER TABLE `especialidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exame`
--

DROP TABLE IF EXISTS `exame`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exame` (
  `id_exame` int NOT NULL AUTO_INCREMENT,
  `nome_exame` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_exame`),
  UNIQUE KEY `nome_exame` (`nome_exame`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exame`
--

LOCK TABLES `exame` WRITE;
/*!40000 ALTER TABLE `exame` DISABLE KEYS */;
/*!40000 ALTER TABLE `exame` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `id_funcionario` int NOT NULL AUTO_INCREMENT,
  `id_cargo` int DEFAULT NULL,
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
  UNIQUE KEY `email` (`email`),
  KEY `id_cargo` (`id_cargo`),
  CONSTRAINT `funcionarios_ibfk_1` FOREIGN KEY (`id_cargo`) REFERENCES `cargo` (`id_cargo`)
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
  `id_cargo` int DEFAULT NULL,
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
  UNIQUE KEY `telefone` (`telefone`),
  KEY `id_cargo` (`id_cargo`),
  CONSTRAINT `medico_ibfk_1` FOREIGN KEY (`id_cargo`) REFERENCES `cargo` (`id_cargo`)
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
-- Table structure for table `solicitacao_exame`
--

DROP TABLE IF EXISTS `solicitacao_exame`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `solicitacao_exame` (
  `id_solicitacao` int NOT NULL AUTO_INCREMENT,
  `id_atendimento` int DEFAULT NULL,
  `id_exame` int DEFAULT NULL,
  PRIMARY KEY (`id_solicitacao`),
  KEY `id_atendimento` (`id_atendimento`),
  KEY `id_exame` (`id_exame`),
  CONSTRAINT `solicitacao_exame_ibfk_1` FOREIGN KEY (`id_atendimento`) REFERENCES `atendimento` (`id_atendimento`),
  CONSTRAINT `solicitacao_exame_ibfk_2` FOREIGN KEY (`id_exame`) REFERENCES `exame` (`id_exame`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitacao_exame`
--

LOCK TABLES `solicitacao_exame` WRITE;
/*!40000 ALTER TABLE `solicitacao_exame` DISABLE KEYS */;
/*!40000 ALTER TABLE `solicitacao_exame` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_atendimento`
--

DROP TABLE IF EXISTS `tipo_atendimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_atendimento` (
  `id_tipo` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_tipo`),
  UNIQUE KEY `nome` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_atendimento`
--

LOCK TABLES `tipo_atendimento` WRITE;
/*!40000 ALTER TABLE `tipo_atendimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_atendimento` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-19 21:21:31
