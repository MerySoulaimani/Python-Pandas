
#Exercice 1
#1.Programme pour définir 3 variables et afficher leur type :
# Définition des variables
str1, int1, dec1 = ("ceci est une chaîne", 12, 15.0)

# Affichage des types
print(type(str1))  # <class 'str'>
print(type(int1))  # <class 'int'>
print(type(dec1))  # <class 'float'>
#2.Exemple similaire pour les informations personnelles 

# Définition des variables
nom, prenom, age = ("Dupont", "Jean", 25)

# Affichage des types
print(type(nom))    # <class 'str'>
print(type(prenom))  # <class 'str'>
print(type(age))     # <class 'int'>


### Exercice 2

#1. **Calcul de la moyenne des notes :**


# Saisie des notes et des coefficients
note_anglais = float(input("Entrez la note d'Anglais : "))
coef_anglais = float(input("Entrez le coefficient d'Anglais : "))

note_physique = float(input("Entrez la note de Physique : "))
coef_physique = float(input("Entrez le coefficient de Physique : "))

note_maths = float(input("Entrez la note de Maths : "))
coef_maths = float(input("Entrez le coefficient de Maths : "))

note_svt = float(input("Entrez la note de SVT : "))
coef_svt = float(input("Entrez le coefficient de SVT : "))

# Calcul de la moyenne
somme_notes = (note_anglais * coef_anglais + note_physique * coef_physique +
               note_maths * coef_maths + note_svt * coef_svt)
somme_coefficients = coef_anglais + coef_physique + coef_maths + coef_svt

moyenne = somme_notes / somme_coefficients
print("La moyenne des notes est :", moyenne)


# 2. **Vérification du budget pour les achats :**


# Saisie du budget et des achats
budget = float(input("Entrez votre budget : "))
achats = float(input("Entrez le montant des achats : "))

# Vérification si le budget permet de payer les achats
if budget >= achats:
    print("Le budget permet de payer les achats.")
else:
    print("Le budget ne permet pas de payer les achats.")


### Exercice 3

#Calcul du volume d'un cône droit :**


import math

# Saisie du rayon et de la hauteur
rayon = float(input("Entrez le rayon du cône : "))
hauteur = float(input("Entrez la hauteur du cône : "))

# Calcul du volume
volume = (1/3) * math.pi * (rayon ** 2) * hauteur
print("Le volume du cône est :", volume)


### Exercice 4

# Calcul de la surface d'un disque découpé :**

import math

# Saisie des rayons
Rg = float(input("Entrez le rayon du disque (Rg) : "))
Rp = float(input("Entrez le rayon du trou (Rp) : "))

# Calcul de la surface du disque découpé
surface_disque = math.pi * (Rg ** 2) - math.pi * (Rp ** 2)
print("La surface du disque découpé est :", surface_disque)

### Exercice 5

#Vérification de la longueur d'une phrase :**
# Saisie d'une phrase
phrase = input("Entrez une phrase : ")

# Vérification de la longueur
longueur = len(phrase)

if longueur % 2 == 0:  # Longueur paire
    moitie = longueur // 2
    print("La première moitié de la phrase est :", phrase[:moitie])
else:  # Longueur impaire
    moitie = longueur // 2 + 1
    print("La seconde moitié de la phrase est :", phrase[moitie:])

