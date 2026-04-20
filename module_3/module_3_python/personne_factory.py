"""
Pattern Factory Method
-----------------------
PersonneFactory : crée des objets Etudiant ou Enseignant
sans exposer la logique d'instanciation au client.

Usage :
    e = PersonneFactory.creer("etudiant", nom="Alice", age=20,
                              numero_etudiant="E001", moyenne=14.0)
    p = PersonneFactory.creer("enseignant", nom="M. Dupont", age=45,
                              matiere="Maths", salaire=3500.0)
"""

from etudiant import Etudiant
from enseignant import Enseignant


class PersonneFactory:
    """
    Fabrique de personnes.
    La méthode de classe creer() joue le rôle de factory method.
    """

    @classmethod
    def creer(cls, type_personne: str, **kwargs):
        """
        Crée et retourne une instance selon le type demandé.

        Paramètres
        ----------
        type_personne : str
            "etudiant" ou "enseignant" (insensible à la casse)
        **kwargs :
            Arguments passés au constructeur de la classe cible.

        Lève
        ----
        ValueError si le type est inconnu.
        """
        type_lower = type_personne.strip().lower()

        if type_lower == "etudiant":
            champs = ("nom", "age", "numero_etudiant", "moyenne")
            cls.__verifier_champs(champs, kwargs, "Etudiant")
            return Etudiant(
                nom=kwargs["nom"],
                age=kwargs["age"],
                numero_etudiant=kwargs["numero_etudiant"],
                moyenne=kwargs["moyenne"],
            )

        elif type_lower == "enseignant":
            champs = ("nom", "age", "matiere", "salaire")
            cls.__verifier_champs(champs, kwargs, "Enseignant")
            return Enseignant(
                nom=kwargs["nom"],
                age=kwargs["age"],
                matiere=kwargs["matiere"],
                salaire=kwargs["salaire"],
            )

        else:
            raise ValueError(
                f"Type inconnu : '{type_personne}'. "
                "Valeurs acceptées : 'etudiant', 'enseignant'."
            )

    @staticmethod
    def __verifier_champs(champs_requis, kwargs, nom_classe):
        manquants = [c for c in champs_requis if c not in kwargs]
        if manquants:
            raise ValueError(
                f"Champs manquants pour créer un {nom_classe} : {manquants}"
            )
