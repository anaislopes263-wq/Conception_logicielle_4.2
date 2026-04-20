"""
Classe Cours
Unité d'enseignement avec nom et professeur responsable.
"""


class Cours:

    def __init__(self, nom_cours, professeur_responsable):
        self.nom_cours = nom_cours
        self.professeur_responsable = professeur_responsable

    def __str__(self):
        return f"Cours : {self.nom_cours} (Prof : {self.professeur_responsable})"

    def __repr__(self):
        return f"Cours({self.nom_cours!r}, {self.professeur_responsable!r})"
