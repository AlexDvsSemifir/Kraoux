# Installation App Formation (IAF)

## Description

Permet l'installation des outils suivants :

- VSCode
- Node JS
- JDK

## Prérequis

- [python >= 3.9](https://www.python.org/downloads/)

## Lancement

1. Executer le script "Setup.bat" en tant qu'administrateur
2. Lorsque vous y êtes invité, laissez vous guider par les fenêtres d'installation programme par programme.

## Ajouter des programmes supplémentaires à l'app

1. Créer une variable constante respectant la nomenclature "URL_DL_" suivi du nom de l'app, qui renvoit vers l'url de téléchargement.
2. Ajouter cette variable à la liste URL_LIST

## Changelog git commit

### Dyn_Install_VSCode

Ajout de l'installation automatisée de VS Code :

- Télécharge l'APP depuis le site dans un dossier "temp" à la racine de C:
- Installe le programme.

### Added_NodeJs

- Ajout de l'installation de NodeJS.
- Création d'une liste pour les URL des sources.
- Adaptation du comportement du code selon le type de source (.exe ou .msi)
- Ajout de messages informatifs.

## Finalized Admin

- Ajout de JDK à la liste des programmes,
- Ajout de "setup.nat" pour lancer le script (à éxecuter en Admin)
- Ajout de pauses pour la pahse de Dev. Seront retirés en même temps que l'update du ReadMe.
- Les modules importés lors des tests seront aussi nettoyés lors de cette même update.

## Random Incoming Features

- Choix des programmes à installer ?
- Full ZTI ?
