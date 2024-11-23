# **Projet Nutrition**

## **Description**

Ce projet a pour objectif de créer un programme (`main.py`) capable de générer des repas éco-responsables en accord avec les besoins nutritionnels du sujet et de ses préférences alimentaires (végétarien ou non) à l’aide d’une interface graphique.

### **Fonctionnalités :**
- Génération de repas éco-responsables en fonction :
  - Des caractéristiques personnelles (poids, taille, niveau d’activité physique, etc.).
  - Des données nutritionnelles et écologiques des aliments.
- Classement des repas possibles selon un **"score environnemental"** allant de **A** (le plus éco-responsable) à **E** (le moins éco-responsable).
- Sortie d’un fichier Excel nommé `repas_possibles.xlsx` contenant tous les repas générés.
- Interface graphique intuitive avec des champs ajustables grâce à une barre de défilement.

---

## **Données Utilisées**

Le programme se base sur deux fichiers principaux :

1. `4-TableS1_augmented_with_FAO_data.xlsx` : Données nutritionnelles des aliments, y compris leurs apports en calories, protéines, lipides, glucides, etc.
2. `5-DataS2.xlsx` : Données sur l’impact environnemental des aliments (émissions de gaz à effet de serre, consommation d’eau, etc.).

---

## **Langages et Outils**

- **Langage :** Python
- **Bibliothèques utilisées :**
  - `Pandas` : Manipulation des données Excel.
  - `NumPy` : Calculs et analyses numériques.
  - `Tkinter` : Création de l’interface graphique.
  - `os` : Gestion des fichiers en entrée/sortie.

---

## **Instructions d’Exécution**
1. **Utilisation de l’interface graphique :**
   - Remplissez les champs affichés dans l’interface (poids, taille, etc.).
   - **Note :** Pour naviguer dans l’interface graphique, utilisez la barre de défilement située à droite (la molette de la souris ne permet pas le défilement sur la page).

2. **Sortie des résultats :**
   - Une fois les champs complétés, le programme génère un fichier Excel nommé **repas_possibles.xlsx**, contenant tous les repas possibles classés selon leur score environnemental.

---

## **Résultats**

- Le fichier **repas_possibles.xlsx** contient :
  - Une liste des repas possibles en accord avec les besoins nutritionnels de l’utilisateur.
  - Un classement des repas selon un score environnemental (de **A** à **E**).

---

