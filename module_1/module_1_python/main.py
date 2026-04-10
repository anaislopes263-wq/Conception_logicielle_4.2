"""
Main : démonstration 

TP1: création d'instances d'étudiants, ajout de cours + détails
TP2: validation et sécurisation des données
TP3: liste hétérogène et affichage des détails pour chacun des éléments

"""

from cours import Cours
from personne import Personne
from etudiant import Etudiant
from enseignant import Enseignant


def separateur(titre):
    print(f"\n{'─' * 45}")
    print(f"  {titre}")
    print(f"{'─' * 45}")



# TP1 — Héritage

separateur("TP1 — Héritage")

TDE = Cours("Décision_estimation", "Mme Quidu")
ML  = Cours("Machine_Learning",  "M. Toumi")
CL  = Cours("Conception_logicielle",      "M. Ba")

anais = Etudiant("anais", 21, "E001", 15.5)
anais.ajouter_cours(TDE)
anais.ajouter_cours(ML)

mathis = Etudiant("mathis", 22, "E002", 17.0)
mathis.ajouter_cours(CL)

print(anais)
print(mathis)

# Vérification de l'héritage
print(f"\nanais est une Personne ? {isinstance(anais, Personne)}")   # True


# TP2 — Encapsulation

separateur("TP2 — Encapsulation")

# Tentative de modifier la moyenne avec une valeur invalide
try:
    anais.moyenne = 25 # impossible car la validation impose une valeur entre 0 et 20
except ValueError as e:
    print(f"Erreur capturée : {e}")

# Tentative de modifier l'âge avec une valeur invalide
try:
    anais.age = -5 # impossible car la validation impose une valeur entre 0 et 100
except ValueError as e:
    print(f"Erreur capturée : {e}")

# Tentative de modifier le numéro étudiant (lecture seule)
try:
    anais.numero_etudiant = "E999" # impossible car il n'y a pas de setter pour cet attribut (lecture seule)
except AttributeError as e:
    print(f"Erreur capturée : numéro étudiant en lecture seule")

# Modification valide
anais.moyenne = 16.0
print(f"\nNouvelle moyenne d'Anais (valide) : {anais.moyenne}/20")


# TP3 — Polymorphisme
separateur("TP3 — Polymorphisme")

prof1 = Enseignant("Mme Martin", 45, "Informatique", 3500.0)
prof2 = Enseignant("M. Dupont",  52, "Mathématiques", 3800.0)

# Liste contenant etudiant et des Enseignant
liste_personnes = [anais, mathis, prof1, prof2]

print("Appel de afficher_details() sur chaque élément :\n")
for personne in liste_personnes:
    print(personne.afficher_details())
    print()
