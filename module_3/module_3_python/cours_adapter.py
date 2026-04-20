"""
Pattern de structure: Adapter

Supposons que vous récupériez des données de cours via un 
ancien système (Legacy) fournissant des données au format "String 
concaténée". Créez un adaptateur pour transformer ces données en objets 
Cours compatibles avec votre système. 
"""

from cours import Cours


class LegacyCoursService:
    """
    Simule l'ancien système (legacy) qui fournit les données
    sous la forme "NomCours|NomProfesseur".
    Cette classe ne doit PAS être modifiée (contrainte legacy).
    """

    def get_cours_brut(self, donnee: str) -> str:
        """Retourne la donnée brute telle quelle (format legacy)."""
        return donnee


class CoursAdapter(Cours):
    """
    Adaptateur : convertit une chaîne legacy "NomCours|NomProfesseur"
    en un objet Cours utilisable par le système courant.
    """

    SEPARATEUR = "|"

    def __init__(self, donnee_legacy: str):
        """
        Paramètre
        ---------
        donnee_legacy : str
            Chaîne au format "NomCours|NomProfesseur"
        """
        self.__legacy_service = LegacyCoursService()
        brut = self.__legacy_service.get_cours_brut(donnee_legacy)
        self.__valider_format(brut)
        parties = brut.split(self.SEPARATEUR, maxsplit=1)
        nom_cours = parties[0].strip()
        professeur = parties[1].strip()
        super().__init__(nom_cours, professeur)

    @staticmethod
    def __valider_format(donnee: str):
        if CoursAdapter.SEPARATEUR not in donnee:
            raise ValueError(
                f"Format legacy invalide : '{donnee}'. "
                f"Attendu : 'NomCours{CoursAdapter.SEPARATEUR}NomProfesseur'"
            )

    def __str__(self):
        return f"[Adapté] {super().__str__()}"
