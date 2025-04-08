
### Exercice 1 : Création et Manipulation de Tableaux

import numpy as np

# Tableau 1D contenant les nombres de 0 à 9
tableau_1D = np.arange(10)
print("Tableau 1D :", tableau_1D)

# Tableau 2D de dimensions (3, 3) avec des nombres aléatoires entre 0 et 1
tableau_2D = np.random.rand(3, 3)
print("Tableau 2D :\n", tableau_2D)

# Tableau 3D de dimensions (2, 3, 4) rempli de zéros
tableau_3D = np.zeros((2, 3, 4))
print("Tableau 3D :\n", tableau_3D)



# Accéder au troisième élément du tableau 1D
element_3D = tableau_1D[2]
print("Troisième élément du tableau 1D :", element_3D)

# Accéder à la deuxième ligne et première colonne du tableau 2D
element_2D = tableau_2D[1, 0]
print("Deuxième ligne, première colonne du tableau 2D :", element_2D)

# Modifier un élément du tableau 3D
tableau_3D[0, 1, 2] = 5
print("Tableau 3D après modification :\n", tableau_3D)

# Récupérer les trois premiers éléments du tableau 1D
premiers_elements_1D = tableau_1D[:3]
print("Trois premiers éléments du tableau 1D :", premiers_elements_1D)

# Prendre la dernière colonne du tableau 2D
derniere_colonne_2D = tableau_2D[:, -1]
print("Dernière colonne du tableau 2D :", derniere_colonne_2D)
### Exercice 2 : Opérations Mathématiques et Logiques
# Création de deux tableaux 1D de longueur 5
tableau_a = np.array([1, 2, 3, 4, 5])
tableau_b = np.array([5, 4, 3, 2, 1])

# Opérations élément par élément
addition = tableau_a + tableau_b
soustraction = tableau_a - tableau_b
multiplication = tableau_a * tableau_b
division = tableau_a / tableau_b

print("Addition :", addition)
print("Soustraction :", soustraction)
print("Multiplication :", multiplication)
print("Division :", division)
# Créer un tableau de valeurs entre 0 et π
valeurs = np.linspace(0, np.pi, 10)

# Appliquer les fonctions trigonométriques et exponentielles
sinus = np.sin(valeurs)
cosinus = np.cos(valeurs)
exponentielle = np.exp(valeurs)

print("Valeurs :", valeurs)
print("Sinus :", sinus)
print("Cosinus :", cosinus)
print("Exponentielle :", exponentielle)
# Créer un tableau d'entiers de longueur 10
tableau_entiers = np.arange(10)

# Sélectionner tous les éléments pairs
elements_pairs = tableau_entiers[tableau_entiers % 2 == 0]
print("Éléments pairs :", elements_pairs)

# Remplacer tous les éléments impairs par -1
tableau_entiers[tableau_entiers % 2 != 0] = -1
print("Tableau après remplacement des impairs par -1 :", tableau_entiers)

### Exercice 3 : Reshaping et Axes

import numpy as np

# Créer un tableau de 12 éléments
tableau_1D = np.arange(12)
print("Tableau 1D :", tableau_1D)

# Transformer en un tableau 2D de dimensions (3, 4)
tableau_2D = tableau_1D.reshape(3, 4)
print("Tableau 2D (3, 4) :\n", tableau_2D)

# Transformer en un tableau 3D de dimensions (2, 2, 3)
tableau_3D = tableau_2D.reshape(2, 2, 3)
print("Tableau 3D (2, 2, 3) :\n", tableau_3D)
# Transposer le tableau 2D
tableau_2D_transpose = tableau_2D.T
print("Tableau 2D transposé :\n", tableau_2D_transpose)

# Appliquer np.swapaxes pour échanger les axes 0 et 1
tableau_2D_swapaxes = np.swapaxes(tableau_2D, 0, 1)
print("Tableau 2D après swapaxes :\n", tableau_2D_swapaxes)
# Créer deux tableaux 2D de dimensions (2, 3)
tableau_A = np.array([[1, 2, 3], [4, 5, 6]])
tableau_B = np.array([[7, 8, 9], [10, 11, 12]])

print("Tableau A :\n", tableau_A)
print("Tableau B :\n", tableau_B)

# Concaténer verticalement
tableau_concat_vertical = np.vstack((tableau_A, tableau_B))
print("Concaténation verticale :\n", tableau_concat_vertical)

# Concaténer horizontalement
tableau_concat_horizontal = np.hstack((tableau_A, tableau_B))
print("Concaténation horizontale :\n", tableau_concat_horizontal)

# Diviser le tableau concaténé en sous-tableaux
sous_tableaux = np.split(tableau_concat_vertical, 2)  # Diviser en 2 sous-tableaux
print("Sous-tableaux après division :")
for i, sous_tableau in enumerate(sous_tableaux):
    print(f"Sous-tableau {i+1} :\n", sous_tableau)
### Exercice 4 : Fonctions Avancées
import numpy as np

# Créer un tableau aléatoire de dimensions (5, 5)
tableau_aleatoire = np.random.rand(5, 5)
print("Tableau aléatoire (5, 5) :\n", tableau_aleatoire)

# Calculer la moyenne, l'écart-type, le minimum et le maximum par ligne et par colonne
moyenne_par_colonne = np.mean(tableau_aleatoire, axis=0)
moyenne_par_ligne = np.mean(tableau_aleatoire, axis=1)

ecart_type_par_colonne = np.std(tableau_aleatoire, axis=0)
ecart_type_par_ligne = np.std(tableau_aleatoire, axis=1)

minimum_par_colonne = np.min(tableau_aleatoire, axis=0)
minimum_par_ligne = np.min(tableau_aleatoire, axis=1)

maximum_par_colonne = np.max(tableau_aleatoire, axis=0)
maximum_par_ligne = np.max(tableau_aleatoire, axis=1)

print("Moyenne par colonne :", moyenne_par_colonne)
print("Moyenne par ligne :", moyenne_par_ligne)
print("Écart-type par colonne :", ecart_type_par_colonne)
print("Écart-type par ligne :", ecart_type_par_ligne)
print("Minimum par colonne :", minimum_par_colonne)
print("Minimum par ligne :", minimum_par_ligne)
print("Maximum par colonne :", maximum_par_colonne)
print("Maximum par ligne :", maximum_par_ligne)

# Créer un tableau de nombres aléatoires
tableau_aleatoire_2 = np.random.rand(10)
print("Tableau aléatoire :\n", tableau_aleatoire_2)

# Trier le tableau dans l'ordre croissant
tableau_trie = np.sort(tableau_aleatoire_2)
print("Tableau trié :\n", tableau_trie)

# Trouver l'indice de l'élément maximum
indice_maximum = np.argmax(tableau_aleatoire_2)
print("Indice de l'élément maximum :", indice_maximum)


# Créer un tableau 1D de longueur 4
tableau_1D = np.array([1, 2, 3, 4])

# Créer un tableau 2D de dimensions (3, 4)
tableau_2D = np.array([[5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16]])

# Multiplier les tableaux en utilisant le broadcasting
resultat = tableau_2D * tableau_1D
print("Résultat de la multiplication avec broadcasting :\n", resultat)


### Exercice 5 : Statistiques et Simulations



# Créer un tableau de données de dimensions (100, 3)
donnees = np.random.rand(100, 3)

# Calculer la matrice de covariance
matrice_covariance = np.cov(donnees, rowvar=False)
print("Matrice de covariance :\n", matrice_covariance)

import matplotlib.pyplot as plt

# Créer un tableau de données sinusoïdales
t = np.linspace(0, 1, 500)  # Temps
frequence = 5  # Fréquence de la sinusoïde
signal = np.sin(2 * np.pi * frequence * t)

# Appliquer la transformation de Fourier
spectre = np.fft.fft(signal)
frequences = np.fft.fftfreq(len(signal), d=t[1] - t[0])

# Afficher le spectre de fréquences
plt.figure(figsize=(10, 5))
plt.plot(frequences[:len(frequences)//2], np.abs(spectre)[:len(spectres)//2])
plt.title("Spectre de fréquences")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# Simuler 1000 lancers de deux dés
lancers = np.random.randint(1, 7, size=(1000, 2))  # Deux dés
somme_lancers = lancers.sum(axis=1)

# Afficher l'histogramme des sommes obtenues
plt.figure(figsize=(10, 5))
plt.hist(somme_lancers, bins=np.arange(2, 14) - 0.5, density=True, alpha=0.7, color='blue')
plt.title("Histogramme des sommes obtenues")

### Exercice 6 : Analyse des Ventes Mensuelles

import numpy as np

# Créer un tableau 2D avec des valeurs aléatoires entre 100 et 1000
ventes = np.random.randint(100, 1001, size=(12, 3))
print("Ventes mensuelles (P1, P2, P3) :\n", ventes)
# Calculer le total des ventes pour chaque produit
total_ventes = np.sum(ventes, axis=0)
print("Total des ventes pour chaque produit (P1, P2, P3) :", total_ventes)
# Calculer la moyenne des ventes mensuelles pour chaque produit
moyenne_ventes = np.mean(ventes, axis=0)
print("Moyenne des ventes mensuelles pour chaque produit (P1, P2, P3) :", moyenne_ventes)
# Identifier le mois ayant les ventes maximales pour chaque produit
mois_max_ventes = np.argmax(ventes, axis=0)
print("Mois avec les ventes maximales pour chaque produit (P1, P2, P3) :", mois_max_ventes + 1)  # +1 pour afficher le mois (1-12)
# Calculer la croissance mensuelle en pourcentage
croissance_mensuelle = np.diff(ventes, axis=0) / ventes[:-1] * 100
print("Croissance mensuelle en pourcentage (P1, P2, P3) :\n", croissance_mensuelle)

# Identifier le mois avec la plus forte croissance pour chaque produit
mois_max_croissance = np.argmax(croissance_mensuelle, axis=0)
print("Mois avec la plus forte croissance pour chaque produit (P1, P2, P3) :", mois_max_croissance + 2)  # +2 pour ajuster l'index
# Créer un tableau 1D contenant la somme des ventes pour chaque mois
somme_ventes_mensuelles = np.sum(ventes, axis=1)
print("Somme des ventes pour chaque mois :", somme_ventes_mensuelles)
