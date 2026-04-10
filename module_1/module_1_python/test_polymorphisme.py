"""
TP3 - Tests de polymorphisme
On vérifie qu'Etudiant et Enseignant ont chacun leur propre afficher_details(),
et qu'on peut les traiter de façon identique via une liste de Personne.
"""
import pytest
from personne import Personne
from etudiant import Etudiant
from enseignant import Enseignant


# Tests de la classe Enseignant

def test_enseignant_creation():
    ens = Enseignant("Mme Martin", 45, "Informatique", 3500.0)
    assert ens.nom == "Mme Martin"
    assert ens.age == 45
    assert ens.matiere == "Informatique"
    assert ens.salaire == 3500.0

def test_enseignant_est_une_personne():
    ens = Enseignant("Mme Martin", 45, "Informatique", 3500.0)
    assert isinstance(ens, Personne)

def test_enseignant_salaire_negatif_interdit():
    with pytest.raises(ValueError):
        Enseignant("Mme Martin", 45, "Informatique", -100)

def test_enseignant_matiere_vide_interdite():
    with pytest.raises(ValueError):
        Enseignant("Mme Martin", 45, "", 3500.0)


# Tests de la méthode afficher_details()

def test_personne_afficher_details():
    p = Personne("Alice", 30)
    details = p.afficher_details()
    assert "Alice" in details
    assert "30" in details

def test_etudiant_afficher_details_contient_base():
    # afficher_details() de Etudiant doit appeler super() → contient nom et age
    e = Etudiant("Bob", 22, "E001", 14.5)
    details = e.afficher_details()
    assert "Bob" in details
    assert "22" in details
    assert "14.5" in details

def test_enseignant_afficher_details_contient_base():
    # afficher_details() de Enseignant doit appeler super() → contient nom et age
    ens = Enseignant("Mme Martin", 45, "Informatique", 3500.0)
    details = ens.afficher_details()
    assert "Mme Martin" in details
    assert "45" in details
    assert "3500" in details
    assert "Informatique" in details


# Tests du polymorphisme : liste hétérogène

def test_liste_heterogene():
    e = Etudiant("Bob", 22, "E001", 14.5)
    ens = Enseignant("Mme Martin", 45, "Informatique", 3500.0)

    # Une seule liste de type Personne contient les deux
    liste = [e, ens]

    # On appelle afficher_details() sans vérifier le type
    resultats = [p.afficher_details() for p in liste]

    assert "Bob" in resultats[0]
    assert "Mme Martin" in resultats[1]

def test_affichage_different_selon_type():
    e = Etudiant("Bob", 22, "E001", 14.5)
    ens = Enseignant("Mme Martin", 45, "Info", 3500.0)

    # L'étudiant affiche sa moyenne, pas son salaire
    assert "14.5" in e.afficher_details()
    assert "3500" not in e.afficher_details()

    # L'enseignant affiche son salaire et sa matière, pas de moyenne
    assert "3500" in ens.afficher_details()
    assert "Info" in ens.afficher_details()
