

### Exercice 1

#1. **Définir une liste nommée `Semaine` contenant les jours de la semaine :**


# Définition de la liste Semaine
Semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
# Affichage de la liste
print(Semaine)


#2. **Remplir la liste `Couleurs` par 5 couleurs différentes et afficher la liste :**


# Définition de la liste Couleurs
Couleurs = ['rouge', 'vert', 'bleu', 'jaune', 'orange']
# Affichage de la liste
print(Couleurs)


# 3. **Définir une liste de 7 réels et afficher les éléments ayant les indices 1, 3 et 5 :**


# Définition de la liste de réels
reels = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
# Affichage des éléments aux indices 1, 3 et 5
print(reels[1])  # 2.2
print(reels[3])  # 4.4
print(reels[5])  # 6.6


### Exercice 2

#1. **Quel est le résultat de `print(mylist[1])` ?**


mylist = ['apple', 'banana', 'cherry']
print(mylist[1])  # Résultat : 'banana'


#2. **Quel est le résultat de `print(mylist[2])` ?**


mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2])  # Résultat : 'banana'


#3. **Compléter par la fonction qui retourne la taille de la liste :**


thislist = ['apple', 'banana', 'cherry']
print(len(thislist))  # Compléter par len, Résultat : 3


#4. **Quel est le résultat de `print(mylist[-1])` ?**


mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])  # Résultat : 'cherry'


#5. **Affiche le second élément de la liste :**


fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Résultat : 'banana'


#6. **Quel est le résultat de `print(mylist[1:4])` ?**


mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])  # Résultat : ['banana', 'cherry', 'orange']


#7. **Compléter pour afficher tous les éléments de la liste :**


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[:])  # Affiche tous les éléments


### Exercice 3

#1. **Créer une liste de matières et afficher la liste :**


matieres = ['Anglais', 'Physique', 'Maths', 'Svt']
print(matieres)


#2. **Ajouter 2 nouvelles matières et afficher la liste :**

matieres.append('Histoire')
matieres.append('Geographie')
print(matieres)


#3. **Afficher les éléments de la liste :**

# a. Les 4 premiers éléments de la liste
print(matieres[:4])  # Affiche les 4 premiers éléments

# b. Les 3 derniers éléments de la liste
print(matieres[-3:])  # Affiche les 3 derniers éléments

# c. 3 éléments depuis le second indice
print(matieres[2:5])  # Affiche 3 éléments depuis le second indice


### Exercice 4

#1. **Quel est le résultat de `print(mylist[1])` après modification ?**


mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])  # Résultat : 'banana'


#2. **Modifier la valeur de « apple » à « kiwi » :**


fruits = ["apple", "banana", "cherry"]
fruits[0] = 'kiwi'  # Modification de 'apple' à 'kiwi'
print(fruits)  # Affiche : ['kiwi