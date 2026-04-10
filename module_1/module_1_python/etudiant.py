"""
Classe Etudiant
Hérite de Personne.

TP1 : ajoute des attributs spécifiques aux étudiants (n° d'étudiant, moyenne, liste de cours).

TP2: rendre les attributs nom, age et moyenne privés + gestion par validation 
(ex: moyenne entre 0 et 20)

TP3: 

"""

from personne import Personne


class Etudiant(Personne):

    def __init__(self, nom, age, numero_etudiant, moyenne):
        super().__init__(nom, age) # Constructeur de la classe mère Personne

        self.__numero_etudiant = numero_etudiant # lecture seule après création (pas de setter)

        self.moyenne = moyenne    # appelle le setter avec validation (valeur entre 0 et 20)
        self.__liste_cours = []   # privée, accessible uniquement via ajouter_cours()

    @property
    def numero_etudiant(self): #en lecture seule comme demandé dans le guide
        return self.__numero_etudiant

    @property
    def moyenne(self): 
        return self.__moyenne

    @moyenne.setter
    def moyenne(self, valeur): #validation: valeur entre 0 et 20 obligatoirement 
        if valeur < 0 or valeur > 20:
            raise ValueError("La moyenne doit être comprise entre 0 et 20.")
        self.__moyenne = valeur

    @property
    def liste_cours(self):
        # On retourne une copie pour empêcher toute modification directe
        return list(self.__liste_cours)

    def ajouter_cours(self, cours): # méthode pour ajouter un cours à la liste de l'étudiant 
        self.__liste_cours.append(cours)


#TP3
    def afficher_details(self):
        # On réutilise la version de Personne via super()
        base = super().afficher_details()
        noms_cours = [c.nom_cours for c in self.__liste_cours]
        return (
            f"{base}\n"
            f"  Moyenne : {self.moyenne}/20\n"
            f"  Cours   : {', '.join(noms_cours) if noms_cours else 'aucun'}"
        )


    def __str__(self):
        noms_cours = [c.nom_cours for c in self.__liste_cours]
        return (
            f"{super().__str__()}\n"
            f"  Numéro étudiant : {self.numero_etudiant}\n"
            f"  Moyenne         : {self.moyenne}/20\n"
            f"  Cours           : {', '.join(noms_cours) if noms_cours else 'aucun'}"
        )

    def __repr__(self):
        return (
            f"Etudiant(nom={self.nom!r}, age={self.age}, "
            f"numero={self.numero_etudiant!r}, moyenne={self.moyenne})"
        )
