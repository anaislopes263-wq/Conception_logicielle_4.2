"""
Classe Etudiant
Hérite de Personne.

Attributs : numéro étudiant (lecture seule), moyenne (validée 0-20), liste de cours.
Implémente le pattern Observer côté sujet :
  - possède une liste d'observateurs
  - notifie lors de l'ajout d'une note via ajouter_note()
"""

from personne import Personne


class Etudiant(Personne):

    def __init__(self, nom, age, numero_etudiant, moyenne):
        super().__init__(nom, age)
        self.__numero_etudiant = numero_etudiant
        self.moyenne = moyenne
        self.__liste_cours = []
        self.__notes = []
        self.__observateurs = []   # pattern Observer : liste des observateurs abonnés

    # ------------------------------------------------------------------ #
    #  Propriétés                                                         
    # ------------------------------------------------------------------ #

    @property
    def numero_etudiant(self):
        return self.__numero_etudiant

    @property
    def moyenne(self):
        return self.__moyenne

    @moyenne.setter
    def moyenne(self, valeur):
        if valeur < 0 or valeur > 20:
            raise ValueError("La moyenne doit être comprise entre 0 et 20.")
        self.__moyenne = valeur

    @property
    def liste_cours(self):
        return list(self.__liste_cours)

    @property
    def notes(self):
        return list(self.__notes)

    # ------------------------------------------------------------------ #
    #  Gestion des cours                                                   #
    # ------------------------------------------------------------------ #

    def ajouter_cours(self, cours):
        """Ajoute un objet Cours à la liste de l'étudiant."""
        self.__liste_cours.append(cours)

    # ------------------------------------------------------------------ #
    #  Pattern Observer — gestion des observateurs                        #
    # ------------------------------------------------------------------ #

    def abonner(self, observateur):
        """Abonne un observateur (ex : ScolariteManager)."""
        if observateur not in self.__observateurs:
            self.__observateurs.append(observateur)

    def desabonner(self, observateur):
        """Désabonne un observateur."""
        self.__observateurs.remove(observateur)

    def notifier(self):
        """Notifie tous les observateurs d'un changement d'état."""
        for obs in self.__observateurs:
            obs.mise_a_jour(self)

    def ajouter_note(self, note):
        """
        Ajoute une note, recalcule la moyenne automatiquement,
        puis notifie les observateurs.
        """
        if note < 0 or note > 20:
            raise ValueError("Une note doit être comprise entre 0 et 20.")
        self.__notes.append(note)
        self.moyenne = sum(self.__notes) / len(self.__notes)
        self.notifier()   # ← déclenchement automatique de l'Observer

    # ------------------------------------------------------------------ #
    #  Affichage                                                           #
    # ------------------------------------------------------------------ #

    def afficher_details(self):
        base = super().__str__()
        noms_cours = [c.nom_cours for c in self.__liste_cours]
        return (
            f"{base}\n"
            f"  Numéro étudiant : {self.numero_etudiant}\n"
            f"  Moyenne         : {self.moyenne:.2f}/20\n"
            f"  Cours           : {', '.join(noms_cours) if noms_cours else 'aucun'}"
        )

    def __str__(self):
        noms_cours = [c.nom_cours for c in self.__liste_cours]
        return (
            f"{super().__str__()}\n"
            f"  Numéro étudiant : {self.numero_etudiant}\n"
            f"  Moyenne         : {self.moyenne:.2f}/20\n"
            f"  Cours           : {', '.join(noms_cours) if noms_cours else 'aucun'}"
        )

    def __repr__(self):
        return (
            f"Etudiant(nom={self.nom!r}, age={self.age}, "
            f"numero={self.numero_etudiant!r}, moyenne={self.moyenne})"
        )
