"""
Classe Enseignant
Hérite de Personne.
Ajoute matiere et salaire (avec validation).
"""

from personne import Personne


class Enseignant(Personne):

    def __init__(self, nom, age, matiere, salaire):
        super().__init__(nom, age)
        self.matiere = matiere
        self.salaire = salaire

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
        base = super().__str__()
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
