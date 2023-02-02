-- MySQL Script generated by MySQL Workbench
-- Thu Dec 29 16:19:17 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db
-- -----------------------------------------------------
-- MYSQL database for IGL TP

-- -----------------------------------------------------
-- Schema db
--
-- MYSQL database for IGL TP
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `db` ;

-- -----------------------------------------------------
-- Table `db`.`Localisation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db`.`Localisation` (
  `id_localisation` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `wilaya` VARCHAR(50) NOT NULL,
  `commune` VARCHAR(50) NOT NULL,
  `adresse` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id_localisation`));


-- -----------------------------------------------------
-- Table `db`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db`.`User` (
  `id_user` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(50) NOT NULL,
  `prenom` VARCHAR(50) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `pswd` VARCHAR(50) NOT NULL,
  `telephone` VARCHAR(10) NOT NULL,
  `id_localisation` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_user`),
  INDEX `fk_User_Localisation1_idx` (`id_localisation` ASC) VISIBLE,
  CONSTRAINT `fk_User_Localisation1`
    FOREIGN KEY (`id_localisation`)
    REFERENCES `db`.`Localisation` (`id_localisation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `db`.`Annonce`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db`.`Annonce` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `categorie` VARCHAR(50) NOT NULL,
  `type` VARCHAR(50) NOT NULL,
  `surface` INT NOT NULL,
  `description` VARCHAR(4000) NOT NULL,
  `prix` DOUBLE NOT NULL,
  `id_user` INT UNSIGNED NOT NULL,
  `id_localisation` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Annonce_User1_idx` (`id_user` ASC) VISIBLE,
  INDEX `fk_Annonce_Localisation1_idx` (`id_localisation` ASC) VISIBLE,
  CONSTRAINT `fk_Annonce_User1`
    FOREIGN KEY (`id_user`)
    REFERENCES `db`.`User` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Annonce_Localisation1`
    FOREIGN KEY (`id_localisation`)
    REFERENCES `db`.`Localisation` (`id_localisation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `db`.`Message`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db`.`Message` (
  `id_photos` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `content` VARCHAR(4000) NOT NULL,
  `id_source` INT UNSIGNED NOT NULL,
  `id_destination` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_photos`, `id_source`, `id_destination`),
  INDEX `fk_Message_User1_idx` (`id_source` ASC) VISIBLE,
  INDEX `fk_Message_User2_idx` (`id_destination` ASC) VISIBLE,
  CONSTRAINT `fk_Message_User1`
    FOREIGN KEY (`id_source`)
    REFERENCES `db`.`User` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Message_User2`
    FOREIGN KEY (`id_destination`)
    REFERENCES `db`.`User` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `db`.`Photos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db`.`Photos` (
  `id_photo` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `image_path` VARCHAR(1024) NOT NULL,
  `Annonce_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_photo`),
  INDEX `fk_Photos_Annonce1_idx` (`Annonce_id` ASC) VISIBLE,
  CONSTRAINT `fk_Photos_Annonce1`
    FOREIGN KEY (`Annonce_id`)
    REFERENCES `db`.`Annonce` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;