Une entreprise propose un outil d'analyse de données en ligne. Au travers d'une interface Web, les
utilisateurs peuvent charger des fichiers de différents formats (CSV, JSON, XML, Parquet) et effectuer des
manipulations et/ou agrégations dessus.
L'entreprise dispose déjà des services suivants.
- Une API REST qui fait office de point d'entrée Backend.
- Un service d'authentification SAML 2.0
- Un service de collecte de logs
Elle souhaite effectuer les tâches de traitements de donné es sur un système scalable avec une file
d'attente pour gérer efficacement les demandes de manipulation de données sans provoquer de goulot
d'é tranglement. Elle cherche dont à cré er un service HTTP permettant d'effectuer ces requêtes à
distances (principe proche de RCP).
Objectifs
Modéliser les objets du service HTTP et construire des diagrammes d'activité.
Développer l'API REST Python en suivant les bonnes pratiques de développement.
Documenter le code de l'API Python.
Authentification
Un autre service permettra d'authentifier les appels. Né anmoins, un jeton d'accès (token JWT) est
nécessaire pour chaque appel API, afin de savoir qu'il est à l'origine d'un calcul.
Pour simplifier, on vérifiera que dans chaque requête (corps ou en-tête), un champ Authorization est
présent et contient la valeur du jeton d'accès, dont la bonne valeur serait codée en dur dans le code de
l'API.
Routes API
- Route health qui retourne le status du serveur.
- Route compute qui applique un traitement sur un DataFrame.
- Chaque requête POST sur compute/... devra lire un fichier sur un disque dur (mentionné en paramètre
de corps JSON). Elle devra écrire le résultat sur le disque dur, et retourner en réponse au client le chemin
d'accès au fichier (format JSON).
- Les opérations suivantes doivent être implémentées : group_by pour regrouper selon une ou plusieurs
colonnes, non_null pour récupérer les valeurs non nulles sur une ou plusieurs colonnes et stats pour
calculer les statistiques classiques (moyenne, variance et écart-type) sur une ou plusieurs colonnes.
Il est supposé (en pratique), que le serveur qui effectuerait les calculs est indépendant du client. Pour
cela, on met en place un système de fichiers distribués (type HDFS) que l'on modélisera, dans le cadre du
projet, par un dossier local où s'exécute l'API.
La notation tiendra compte des aspects suivants :

14 points Code de l'API.

8 points Modélisation des routes et vérification de l'identité à chaque requête.

2 points Structuration du projet pertinente (PEP8, documentation type Docstring).

2 points Tests unitaires de l'API.

6 points Présentation orale.

1 point Exécution valide en direct de l'API.

1 point Respect du temps imparti et répartition du temps de parole.

4 points Pertinence de l'exposé oral.