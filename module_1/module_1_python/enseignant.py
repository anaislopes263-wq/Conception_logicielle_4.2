"""
Classe Enseignant 
Hérite de Personne. 
TP3 : Ajoute matiere et salaire.
afficher_details() redéfinie, appelle super().
"""

from personne import Personne


class Enseignant(Personne):

    def __init__(self, nom, age, matiere, salaire):
        # Constructeur de la classe mère
        super().__init__(nom, age)

        self.matiere = matiere    # appelle le setter
        self.salaire = salaire    # appelle le setter avec validation

    @property
    def matiere(self):
        return self.__matiere

    @matiere.setter
    def matiere(self, valeur):
        if not valeur or not valeur.strip():
            raise ValueError("La matière ne peut pas être vide.")
        self.__matiere = valeur


    @property
    def salaire(self):
        return self.__salaire

    @salaire.setter
    def salaire(self, valeur):
        if valeur < 0:
            raise ValueError("Le salaire ne peut pas être négatif.")
        self.__salaire = valeur


    def afficher_details(self):
        # On réutilise la version de Personne via super(). C'est un override
        base = super().afficher_details()
        return (
            f"{base}\n"
            f"  Matière : {self.matiere}\n"
            f"  Salaire : {self.salaire} €"
        )


    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"  Matière : {self.matiere}\n"
            f"  Salaire : {self.salaire} €"
        )
