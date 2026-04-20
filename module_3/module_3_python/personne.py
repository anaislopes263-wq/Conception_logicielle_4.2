"""
Classe Personne
Classe mère abstraite.

Attributs nom et age privés avec validation.
Méthode afficher_details() redéfinie dans les sous-classes.
"""

from abc import ABC, abstractmethod


class Personne(ABC):

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, valeur):
        if not valeur or not valeur.strip():
            raise ValueError("Le nom ne peut pas être vide.")
        self.__nom = valeur

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, valeur):
        if valeur <= 0 or valeur >= 100:
            raise ValueError("L'âge doit être strictement entre 0 et 100.")
        self.__age = valeur

    @abstractmethod
    def afficher_details(self):
        pass

    def __str__(self):
        return f"{self.nom}, {self.age} ans"
