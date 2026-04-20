"""
Main
==========================================

Ce fichier illustre les 6 patterns demandés dans le TP :

  Création   : 1. Singleton (ScolariteManager)
               2. Factory Method (PersonneFactory)
  Structure  : 3. Decorator (EtudiantBoursier, EtudiantDelegue)
               4. Adapter (CoursAdapter)
  Comportement: 5. Strategy (TriParMoyenne, TriParNom, TriParAge)
               6. Observer (Etudiant notifie ScolariteManager)
"""

from cours import Cours
from cours_adapter import CoursAdapter
from etudiant_decorateur import EtudiantBoursier, EtudiantDelegue
from personne_factory import PersonneFactory
from scolarite_manager import ScolariteManager
from strategie_tri import GestionnaireTriEtudiants, TriParMoyenne, TriParNom, TriParAge


def separateur(titre):
    print(f"\n{'═' * 50}")
    print(f"  {titre}")
    print(f"{'═' * 50}")


#  PATTERN 1 — Singleton                             

separateur("PATTERN 1 — Singleton : ScolariteManager")

manager_a = ScolariteManager()
manager_b = ScolariteManager()
print(f"manager_a is manager_b : {manager_a is manager_b}")   # True attendu
print(f"Instance unique : {manager_a}")


#  PATTERN 2 — Factory Method                        

separateur("PATTERN 2 — Factory Method : PersonneFactory")

anais  = PersonneFactory.creer("etudiant",   nom="Anais",   age=21,
                                numero_etudiant="E001", moyenne=15.5)
mathis = PersonneFactory.creer("etudiant",   nom="Mathis",  age=22,
                                numero_etudiant="E002", moyenne=17.0)
leo    = PersonneFactory.creer("etudiant",   nom="Leo",     age=20,
                                numero_etudiant="E003", moyenne=11.0)
prof   = PersonneFactory.creer("enseignant", nom="Mme Martin", age=45,
                                matiere="Informatique", salaire=3500.0)

print("Objets créés via la factory :")
print(f"  {anais.nom}  → {type(anais).__name__}")
print(f"  {mathis.nom} → {type(mathis).__name__}")
print(f"  {prof.nom}  → {type(prof).__name__}")

# Test type inconnu
try:
    PersonneFactory.creer("inconnu", nom="X", age=30)
except ValueError as e:
    print(f"  Erreur capturée : {e}")



#  PATTERN 4 — Adapter    

separateur("PATTERN 4 — Adapter : CoursAdapter (données legacy)")

# Cours créés de manière classique
cours_cl  = Cours("Conception_logicielle", "M. Ba")
cours_tde = Cours("Décision_estimation",   "Mme Quidu")

# Cours créés via l'adaptateur (données issues d'un système legacy)
cours_ml   = CoursAdapter("Machine_Learning|M. Toumi")
cours_algo = CoursAdapter("Algorithmique|M. Leroy")

print(f"  Cours standard  : {cours_cl}")
print(f"  Cours adapté    : {cours_ml}")
print(f"  Cours adapté    : {cours_algo}")

# Test format invalide
try:
    CoursAdapter("FormatInvalide")
except ValueError as e:
    print(f"  Erreur capturée : {e}")

# Ajout des cours aux étudiants
anais.ajouter_cours(cours_tde)
anais.ajouter_cours(cours_ml)
mathis.ajouter_cours(cours_cl)
leo.ajouter_cours(cours_algo)
leo.ajouter_cours(cours_cl)



#  PATTERN 3 — Decorator                             

separateur("PATTERN 3 — Decorator : EtudiantBoursier & EtudiantDelegue")

anais_boursiere = EtudiantBoursier(anais, montant_bourse=450.0)
mathis_delegue  = EtudiantDelegue(mathis, promotion="ENSTA 2025")

# Combinaison des deux décorateurs sur un même étudiant
leo_boursier_delegue = EtudiantDelegue(
    EtudiantBoursier(leo, montant_bourse=300.0),
    promotion="ENSTA 2026"
)

print("─ Anais (boursière) ─")
print(anais_boursiere.afficher_details())
print()
print("─ Mathis (délégué) ─")
print(mathis_delegue.afficher_details())
print()
print("─ Leo (boursier + délégué) ─")
print(leo_boursier_delegue.afficher_details())



#  PATTERN 6 — Observer                              

separateur("PATTERN 6 — Observer : notification au ScolariteManager")

manager = ScolariteManager()   # même instance Singleton
manager.inscrire_etudiant(anais)
manager.inscrire_etudiant(mathis)
manager.inscrire_etudiant(leo)

print("État initial :")
manager.afficher_statistiques()

print("\nAjout de notes → le ScolariteManager est automatiquement notifié :")
anais.ajouter_note(18.0)
anais.ajouter_note(14.0)
mathis.ajouter_note(16.5)
leo.ajouter_note(9.0)

print("\nStatistiques après mise à jour :")
manager.afficher_statistiques()



#  PATTERN 5 — Strategy                              

separateur("PATTERN 5 — Strategy : tri dynamique des étudiants")

liste_etudiants = manager.etudiants
gestionnaire = GestionnaireTriEtudiants(TriParMoyenne())

print("Tri par moyenne :")
for e in gestionnaire.trier(liste_etudiants):
    print(f"  {e.nom} → {e.moyenne:.2f}/20")

# Changement dynamique de stratégie
gestionnaire.changer_strategie(TriParNom())
print("\nTri par nom :")
for e in gestionnaire.trier(liste_etudiants):
    print(f"  {e.nom} → {e.moyenne:.2f}/20")

gestionnaire.changer_strategie(TriParAge())
print("\nTri par âge :")
for e in gestionnaire.trier(liste_etudiants):
    print(f"  {e.nom} ({e.age} ans) → {e.moyenne:.2f}/20")
