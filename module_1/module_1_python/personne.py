"""
Classe Personne 
Classe mère.

TP1 : attributs nom et age. Informations de base pour chaque individu.
TP2 : validation (ex: age entre 0 et 100, nom non vide).

TP3 : 

Classe mère. Attributs nom et age privés avec validation.
Méthode afficher_details() redéfinie dans les sous-classes (TP3).
"""


class Personne:

    def __init__(self, nom, age):
        # On passe par les setters pour déclencher la validation dès la création
        self.nom = nom 
        self.age = age

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, valeur):
        #nom ne peut pas être vide ou ne contenir que des espaces
        if not valeur or not valeur.strip(): 
            raise ValueError("Le nom ne peut pas être vide.")
        self.__nom = valeur


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, valeur):
        # age strictement entre 0 et 100
        if valeur <= 0 or valeur >= 100:
            raise ValueError("L'âge doit être strictemententre 0 et 100.")
        self.__age = valeur



#TP3
    def afficher_details(self):
        return f"{self.nom}, {self.age} ans"

    def __str__(self):
        return f"{self.nom}, {self.age} ans"
