"""
Pattern de comportement: Strategy

Permet de définir une famille d'algorithmes de tri/calcul,
de les encapsuler et de les rendre interchangeables dynamiquement.

  - TriParMoyenne  : tri décroissant par moyenne
  - TriParNom      : tri alphabétique par nom
  - TriParAge      : tri croissant par âge

"""

from abc import ABC, abstractmethod


#  Interface commune (Strategy)                                        #

class StrategieTri(ABC):
    """Interface abstraite pour toutes les stratégies de tri."""

    @abstractmethod
    def trier(self, etudiants: list) -> list:
        """
        Trie et retourne une nouvelle liste d'étudiants.
        La liste originale n'est pas modifiée.
        """
        pass

    @abstractmethod
    def description(self) -> str:
        """Retourne une description de la stratégie."""
        pass


#  Stratégies concrètes                                                


class TriParMoyenne(StrategieTri):
    """Tri décroissant par moyenne (meilleur étudiant en premier)."""

    def trier(self, etudiants: list) -> list:
        return sorted(etudiants, key=lambda e: e.moyenne, reverse=True)

    def description(self) -> str:
        return "Tri par moyenne décroissante"


class TriParNom(StrategieTri):
    """Tri alphabétique croissant par nom."""

    def trier(self, etudiants: list) -> list:
        return sorted(etudiants, key=lambda e: e.nom.lower())

    def description(self) -> str:
        return "Tri par nom alphabétique"


class TriParAge(StrategieTri):
    """Tri croissant par âge."""

    def trier(self, etudiants: list) -> list:
        return sorted(etudiants, key=lambda e: e.age)

    def description(self) -> str:
        return "Tri par âge croissant"



#  Contexte (utilise la stratégie)                                     


class GestionnaireTriEtudiants:
    """
    Contexte du pattern Strategy.
    Délègue le tri à la stratégie injectée, modifiable dynamiquement.
    """

    def __init__(self, strategie: StrategieTri):
        self.__strategie = strategie

    def changer_strategie(self, strategie: StrategieTri):
        """Permet de changer la stratégie à la volée."""
        self.__strategie = strategie

    def trier(self, etudiants: list) -> list:
        """Applique la stratégie courante et retourne la liste triée."""
        print(f"  [Strategy] Stratégie utilisée : {self.__strategie.description()}")
        return self.__strategie.trier(etudiants)
