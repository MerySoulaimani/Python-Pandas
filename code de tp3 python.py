

### Exercice 1

#1. **Écrire une liste des nombres suivants : 4, 8, 15, 16, 23, 42**


# Définition de la liste
nombres = [4, 8, 15, 16, 23, 42]
print(nombres)


#2. **Écrire une fonction `affListe` qui prend une liste en paramètre et affiche chaque élément de la liste :**

def affListe(liste):
    for element in liste:
        print(element)

# Appel de la fonction
affListe(nombres)


### Exercice 2

#1. **Écrire une fonction `somme_liste(liste)` qui retourne la somme des éléments d’une liste :**


def somme_liste(liste):
    return sum(liste)

# Test de la fonction
somme = somme_liste(nombres)
print("Somme des éléments :", somme)


#2. **Ajouter une autre fonction `moyenne_liste(liste)` qui calcule et retourne la moyenne des éléments :**

def moyenne_liste(liste):
    return somme_liste(liste) / len(liste)

# Test de la fonction
moyenne = moyenne_liste(nombres)
print("Moyenne des éléments :", moyenne)


### Exercice 3

#1. **Écrire une fonction `extraire_pairs(liste)` qui retourne une nouvelle liste contenant uniquement les nombres pairs de la liste donnée :**

def extraire_pairs(liste):
    return [x for x in liste if x % 2 == 0]


#2. **Tester cette fonction avec la liste `nombres` :**

nombres_pairs = extraire_pairs(nombres)

#3. **Afficher la liste des nombres pairs retournée :**

print("Nombres pairs :", nombres_pairs)

### Exercice 4

#1. **Écrire une fonction `element_existe(liste, element)` qui vérifie si un élément donné existe dans une liste :**

def element_existe(liste, element):
    return element in liste

#2. **Tester cette fonction :**

# Test avec l'élément 15
print("15 existe dans la liste :", element_existe(nombres, 15))  # True

# Test avec l'élément 50
print("50 existe dans la liste :", element_existe(nombres, 50))  # False

### Exercice 5

#1. **Écrire une fonction `liste_carres(liste)` qui retourne une nouvelle liste contenant les carrés des éléments de la liste d'entrée :**
def liste_carres(liste):
    return [x ** 2 for x in liste]

#2. **Tester cette fonction avec la liste `nombres` :**
carres = liste_carres(nombres)

#3. **Afficher la liste des carrés retournée :**
print("Liste des carrés :", carres)

### Exercice 6

#1. **Écrire une fonction `trouver_min_max(liste)` qui retourne le minimum et le maximum d'une liste sous forme d’un tuple (min, max) :**

def trouver_min_max(liste):
    return (min(liste), max(liste))


#2. **Tester cette fonction avec la liste `nombres` :**

min_max = trouver_min_max(nombres)
print("Minimum et maximum :", min_max)

### Exercice 7

#1. **Créer une deuxième liste appelée `autres_nombres` :**

autres_nombres = [7, 11, 19, 24, 33]


#2. **Écrire une fonction `fusionner_et_trier(liste1, liste2)` qui fusionne deux listes et retourne une nouvelle liste triée :**

def fusionner_et_trier(liste1, liste2):
    return sorted(liste1 + liste2)


#3. **Tester cette fonction avec `nombres` et `autres_nombres` :**

nombres_fusionnes = fusionner_et_trier(nombres, autres_nombres)
print("Liste fusionnée et triée :", nombres_fusionnes)

### Exercice 8

def est_palindrome(mot):
    # On compare le mot original avec son inverse
    return mot == mot[::-1]

# Tests
mots = ["radar", "python", "level"]

for mot in mots:
    if est_palindrome(mot):
        print(f'"{mot}" est un palindrome.')
    else:
        print(f'"{mot}" n\'est pas un palindrome.')
