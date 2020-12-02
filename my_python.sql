-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 02 déc. 2020 à 17:37
-- Version du serveur :  10.4.13-MariaDB
-- Version de PHP : 7.2.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `my_python`
--

-- --------------------------------------------------------

--
-- Structure de la table `atb`
--

CREATE TABLE `atb` (
  `id` int(11) NOT NULL,
  `type` varchar(20) DEFAULT NULL,
  `date` varchar(20) NOT NULL,
  `sujet` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `log_mesg` text NOT NULL,
  `recommandation` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `atb`
--

INSERT INTO `atb` (`id`, `type`, `date`, `sujet`, `description`, `log_mesg`, `recommandation`) VALUES
(1, 'COD', '', '', '', '', ''),
(2, 'LOG', '', '', '', '', ''),
(3, 'COD', '', 'User account locked out (multiple login errors)', '', '', ''),
(4, NULL, '', '', '', '', ''),
(5, 'type', '', 'description', '', '', ''),
(6, 'SPA', '', 'nuyuu', '', '', ''),
(7, 'SPA', 'Un chercheur  des fa', '2020-12-02', 'ffffffff', 'htsyrez\'r', 'fffffffff');

-- --------------------------------------------------------

--
-- Structure de la table `wazuh`
--

CREATE TABLE `wazuh` (
  `id` int(11) NOT NULL,
  `type` varchar(25) NOT NULL,
  `description` varchar(200) NOT NULL,
  `client` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `atb`
--
ALTER TABLE `atb`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `wazuh`
--
ALTER TABLE `wazuh`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `atb`
--
ALTER TABLE `atb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `wazuh`
--
ALTER TABLE `wazuh`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
