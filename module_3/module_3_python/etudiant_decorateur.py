"""
Pattern de structure:Decorator

Permet d'ajouter dynamiquement des responsabilités à un objet Etudiant
sans modifier la classe Etudiant originale.

on peut avoir étudiant boursier, délégué et on peut combiner les 2

"""

from etudiant import Etudiant


class EtudiantDecorateurBase:
    """
    Décorateur de base : délègue tous les appels à l'objet enveloppé.
    Les sous-classes surchargent uniquement ce qu'elles enrichissent.
    """

    def __init__(self, etudiant):
        self._etudiant = etudiant   # objet Etudiant (ou décorateur) enveloppé

    # Délégation des propriétés essentielles
    @property
    def nom(self):
        return self._etudiant.nom

    @property
    def age(self):
        return self._etudiant.age

    @property
    def numero_etudiant(self):
        return self._etudiant.numero_etudiant

    @property
    def moyenne(self):
        return self._etudiant.moyenne

    @property
    def liste_cours(self):
        return self._etudiant.liste_cours

    def ajouter_cours(self, cours):
        self._etudiant.ajouter_cours(cours)

    def ajouter_note(self, note):
        self._etudiant.ajouter_note(note)

    def afficher_details(self):
        return self._etudiant.afficher_details()

    def __str__(self):
        return str(self._etudiant)


class EtudiantBoursier(EtudiantDecorateurBase):
    """
    Décorateur : ajoute le statut boursier à un étudiant.
    Enrichit afficher_details() avec le montant de la bourse.
    """

    def __init__(self, etudiant, montant_bourse: float):
        super().__init__(etudiant)
        if montant_bourse < 0:
            raise ValueError("Le montant de la bourse ne peut pas être négatif.")
        self.__montant_bourse = montant_bourse

    @property
    def montant_bourse(self):
        return self.__montant_bourse

    def afficher_details(self):
        base = self._etudiant.afficher_details()
        return (
            f"{base}\n"
            f"  [Boursier] Bourse mensuelle : {self.__montant_bourse:.2f} €"
        )

    def __str__(self):
        return (
            f"{self._etudiant}\n"
            f"  [Boursier] Bourse mensuelle : {self.__montant_bourse:.2f} €"
        )


class EtudiantDelegue(EtudiantDecorateurBase):
    """
    Décorateur : ajoute le rôle de délégué de promotion.
    Enrichit afficher_details() avec la promotion représentée.
    """

    def __init__(self, etudiant, promotion: str):
        super().__init__(etudiant)
        if not promotion or not promotion.strip():
            raise ValueError("La promotion ne peut pas être vide.")
        self.__promotion = promotion

    @property
    def promotion(self):
        return self.__promotion

    def afficher_details(self):
        base = self._etudiant.afficher_details()
        return (
            f"{base}\n"
            f"  [Délégué] Représentant de la promotion : {self.__promotion}"
        )

    def __str__(self):
        return (
            f"{self._etudiant}\n"
            f"  [Délégué] Représentant de la promotion : {self.__promotion}"
        )
