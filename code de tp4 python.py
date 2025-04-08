

### Exercice 1 : Manipulation de dictionnaires

def gestion_dictionnaire():
    personnes = {}

    while True:
        action = input("Voulez-vous ajouter (a), rechercher (r) ou supprimer (s) une personne ? (q pour quitter) : ").lower()
        
        if action == 'a':
            entree = input("Entrez le nom et l'âge sous la forme Nom:Âge : ")
            nom, age = entree.split(':')
            personnes[nom] = int(age)
            print(f"{nom} a été ajouté avec l'âge {age}.")
        
        elif action == 'r':
            nom = input("Entrez le nom à rechercher : ")
            if nom in personnes:
                print(f"L'âge de {nom} est {personnes[nom]}.")
            else:
                print(f"{nom} n'est pas dans le dictionnaire.")
        
        elif action == 's':
            nom = input("Entrez le nom à supprimer : ")
            if nom in personnes:
                del personnes[nom]
                print(f"{nom} a été supprimé.")
            else:
                print(f"{nom} n'est pas dans le dictionnaire.")
        
        elif action == 'q':
            break
        
        else:
            print("Action non reconnue. Veuillez réessayer.")

    print("Dictionnaire final :", personnes)

# Appel de la fonction
gestion_dictionnaire()


### Exercice 2 : Fusion et tri de dictionnaires

def fusionner_dictionnaires(d1, d2):
    d3 = {}
    
    for key in d1.keys():
        d3[key] = d1[key]
    
    for key in d2.keys():
        if key in d3:
            if isinstance(d3[key], (int, float)) and isinstance(d2[key], (int, float)):
                d3[key] += d2[key]
            elif isinstance(d3[key], str) and isinstance(d2[key], str):
                d3[key] += d2[key]
        else:
            d3[key] = d2[key]
    
    return dict(sorted(d3.items()))

# Exemple d'utilisation
d1 = {"a": 10, "b": "test"}
d2 = {"a": 5, "c": "data"}
resultat = fusionner_dictionnaires(d1, d2)
print(resultat)  # Résultat : {"a": 15, "b": "test", "c": "data"}


### Exercice 3 : Lecture et écriture dans un fichier

def ecrire_fichier(nom_fichier):
    with open(nom_fichier, 'w') as f:
        while True:
            entree = input("Entrez le nom et l'âge sous la forme Nom,Âge (ou 'q' pour quitter) : ")
            if entree.lower() == 'q':
                break
            f.write(entree + '\n')

def lire_fichier(nom_fichier):
    dictionnaire = {}
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            nom, age = ligne.strip().split(',')
            dictionnaire[nom] = int(age)
    return dictionnaire

def modifier_enregistrement(nom_fichier):
    dictionnaire = lire_fichier(nom_fichier)
    nom = input("Entrez le nom à modifier ou ajouter : ")
    age = input("Entrez l'âge : ")
    dictionnaire[nom] = int(age)

    with open(nom_fichier, 'w') as f:
        for nom, age in dictionnaire.items():
            f.write(f"{nom},{age}\n")

# Exemple d'utilisation
nom_fichier = 'noms_ages.txt'
ecrire_fichier(nom_fichier)
dictionnaire = lire_fichier(nom_fichier)
print("Dictionnaire lu :", dictionnaire)
modifier_enregistrement(nom_fichier)

### Exercice 4 : Analyse de données depuis un fichier
def lire_notes(nom_fichier):
    notes = {}
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            nom, note = ligne.strip().split(',')
            notes[nom] = float(note)
    return notes

def calculer_moyenne(notes):
    return sum(notes.values()) / len(notes)

def afficher_etudiants_superieurs(notes, moyenne):
    for nom, note in notes.items():
        if note > moyenne:
            print(f"{nom} a une note supérieure à la moyenne : {note}")

# Exemple d'utilisation
nom_fichier = 'notes_etudiants.txt'
notes = lire_notes(nom_fichier)
moyenne = calculer_moyenne(notes)
print("Moyenne des notes :", moyenne)


### Exercice 5 : Introduction à la POO - Classe Étudiant

#1. **Définir une classe `Etudiant` avec les attributs `nom`, `âge` et `note` :**

class Etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = note

    def afficher_info(self):
        print(f"Nom: {self.nom}, Âge: {self.age}, Note: {self.note}")

    @staticmethod
    def moyenne_notes(etudiants):
        if not etudiants:
            return 0
        total_notes = sum(etudiant.note for etudiant in etudiants)
        return total_notes / len(etudiants)

# Exemple d'utilisation
etudiant1 = Etudiant("Alice", 20, 15.5)
etudiant2 = Etudiant("Bob", 22, 17.0)
etudiant3 = Etudiant("Charlie", 21, 14.0)

etudiants = [etudiant1, etudiant2, etudiant3]

# Afficher les informations des étudiants
for etudiant in etudiants:
    etudiant.afficher_info()

# Calculer la moyenne des notes
moyenne = Etudiant.moyenne_notes(etudiants)
print("Moyenne des notes :", moyenne)


### Exercice 6 : Gestion d’un carnet d’adresses

#1. **Créer une classe `CarnetAdresses` qui utilise un dictionnaire pour stocker des informations (nom, email, téléphone) :**


class CarnetAdresses:
    def __init__(self):
        self.contacts = {}

    def ajouter_contact(self, nom, email, telephone):
        self.contacts[nom] = {'email': email, 'telephone': telephone}
        print(f"Contact {nom} ajouté.")

    def supprimer_contact(self, nom):
        if nom in self.contacts:
            del self.contacts[nom]
            print(f"Contact {nom} supprimé.")
        else:
            print(f"Contact {nom} non trouvé.")

    def rechercher_contact(self, nom):
        contact = self.contacts.get(nom)
        if contact:
            print(f"Contact trouvé : {nom}, Email: {contact['email']}, Téléphone: {contact['telephone']}")
        else:
            print(f"Contact {nom} non trouvé.")

    def sauvegarder_contacts(self, nom_fichier):
        with open(nom_fichier, 'w') as f:
            for nom, info in self.contacts.items():
                f.write(f"{nom},{info['email']},{info['telephone']}\n")
        print("Contacts sauvegardés.")

    def charger_contacts(self, nom_fichier):
        try:
            with open(nom_fichier, 'r') as f:
                for ligne in f:
                    nom, email, telephone = ligne.strip().split(',')
                    self.ajouter_contact(nom, email, telephone)
            print("Contacts chargés.")
        except FileNotFoundError:
            print("Fichier non trouvé.")

# Exemple d'utilisation
carnet = CarnetAdresses()
carnet.ajouter_contact("Alice", "alice@example.com", "123456789")
carnet.ajouter_contact("Bob", "bob@example.com", "987654321")
carnet.rechercher_contact("Alice")
carnet.sauvegarder_contacts("contacts.txt")
carnet.charger_contacts("contacts.txt")


### Exercice 7 : Simulation d’une bibliothèque

#1. **Créer une classe `Livre` avec les attributs `titre`, `auteur` et `statut` (disponible/emprunté) :**

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.statut = "disponible"

    def emprunter(self):
        if self.statut == "disponible":
            self.statut = "emprunté"
            print(f"{self.titre} a été emprunté.")
        else:
            print(f"{self.titre} est déjà emprunté.")

    def rendre(self):
        if self.statut == "emprunté":
            self.statut = "disponible"
            print(f"{self.titre} a été rendu.")
        else:
            print(f"{self.titre} est déjà disponible.")

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"{livre.titre} a été ajouté à la bibliothèque.")

    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                livre.emprunter()
                return
        print(f"{titre} n'est pas disponible dans la bibliothèque.")

    def rendre_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                livre.rendre()
                return
        print(f"{titre} n'est pas dans la bibliothèque.")

    def lister_livres_disponibles(self):
        print("Livres disponibles :")
        for livre in self.livres:
            if livre.statut == "disponible":
                print(f"- {livre.titre} par {livre.auteur}")

# Exemple d'utilisation
bibliotheque = Bibliotheque()
# Ajout de livres
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
livre2 = Livre("1984", "George Orwell")
livre3 = Livre("Moby Dick", "Herman Melville")

bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

# Lister les livres disponibles
bibliotheque.lister_livres_disponibles()

# Emprunter un livre
bibliotheque.emprunter_livre("1984")

# Lister les livres disponibles après emprunt
bibliotheque.lister_livres_disponibles()

# Rendre un livre
bibliotheque.rendre_livre("1984")

# Lister les livres disponibles après retour
bibliotheque.lister_livres_disponibles()
