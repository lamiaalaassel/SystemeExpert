# Système Expert

Ce programme implémente un système expert qui permet de diagnostiquer les pannes potentielles d'un ordinateur en fonction des symptômes fournis par l'utilisateur. Il propose deux modes d'utilisation : Mode Utilisateur et Mode Expert.

## Utilisation

### Mode Utilisateur

Le Mode Utilisateur permet à l'utilisateur de saisir les symptômes observés sur l'ordinateur, puis le système expert analyse ces symptômes pour déterminer les organes potentiellement défectueux.

Pour exécuter le Mode Utilisateur, lancez le programme et sélectionnez l'option "Mode Utilisateur".

### Mode Expert

Le Mode Expert permet à un expert d'ajouter, de modifier ou de supprimer des pannes dans la base de connaissances du système expert. Il fournit également une fonctionnalité pour afficher toutes les pannes répertoriées avec leurs causes associées.

Pour accéder au Mode Expert, vous devez d'abord vous connecter en tant qu'expert à l'aide d'un nom d'utilisateur et d'un mot de passe.

Pour exécuter le Mode Expert, lancez le programme et sélectionnez l'option "Mode Expert", puis connectez-vous en tant qu'expert.

## Fonctionnalités

### Ajouter Panne

Dans le Mode Expert, vous pouvez ajouter une nouvelle panne en spécifiant son nom et ses causes.

### Modifier Panne

Dans le Mode Expert, vous pouvez modifier une panne existante en spécifiant son ancien nom, son nouveau nom et ses nouvelles causes.

### Supprimer Panne

Dans le Mode Expert, vous pouvez supprimer une panne existante en spécifiant son nom.

### Afficher Pannes

Dans le Mode Expert, vous pouvez afficher toutes les pannes répertoriées avec leurs causes associées.

## Fichiers

- `experts.txt`: Ce fichier contient les informations d'identification des experts (noms d'utilisateur et mots de passe). Les experts peuvent se connecter en utilisant ces informations pour accéder au Mode Expert.

## Dépendances

- `tkinter`: Utilisé pour l'interface graphique.
- `ttkthemes`: Utilisé pour les thèmes personnalisés dans l'interface graphique.
## Exécution du code 
-Tapez 'python SE.py' pour exécuter le code.
