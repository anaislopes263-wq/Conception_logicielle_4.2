"""
Classe Cours 

TP1 : représente un cours avec son nom et son professeur responsable.
"""

class Cours:

    def __init__(self, nom_cours, professeur_responsable):
        self.nom_cours = nom_cours
        self.professeur_responsable = professeur_responsable

    def __str__(self):
        return f"Cours : {self.nom_cours} (Prof : {self.professeur_responsable})"
