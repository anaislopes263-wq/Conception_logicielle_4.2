"""
TP1 - Tests d'héritage
On écrit les tests AVANT le code (méthode TDD - phase RED)

Commande à utiliser: python -m pytest -v
"""
import pytest
from cours import Cours
from personne import Personne
from etudiant import Etudiant


# Tests de la classe Cours

def test_cours_creation():
    c = Cours("Estimation_parcimonie", "Mme Dremeau")
    assert c.nom_cours == "Estimation_parcimonie"
    assert c.professeur_responsable == "Mme Dremeau"

def test_cours_str():
    c = Cours("Machine_learning", "M. Toumi")
    assert "Machine_learning" in str(c)
    assert "M. Toumi" in str(c)


# Tests de la classe Personne

def test_personne_creation():
    p = Personne("Alice", 20)
    assert p.nom == "Alice"
    assert p.age == 20

def test_personne_str():
    p = Personne("Alice", 20)
    assert "Alice" in str(p)
    assert "20" in str(p)


# Tests de la classe Etudiant

def test_etudiant_creation():
    e = Etudiant("Bob", 22, "E001", 14.5)
    assert e.nom == "Bob"
    assert e.age == 22
    assert e.numero_etudiant == "E001"
    assert e.moyenne == 14.5

def test_etudiant_est_une_personne():
    e = Etudiant("Bob", 22, "E001", 14.5)
    # Un étudiant DOIT être une instance de Personne (héritage)
    assert isinstance(e, Personne)

def test_etudiant_ajouter_cours():
    e = Etudiant("Bob", 22, "E001", 14.5)
    c = Cours("Info", "M. Durand")
    e.ajouter_cours(c)
    assert len(e.liste_cours) == 1

def test_etudiant_ajouter_plusieurs_cours():
    e = Etudiant("Bob", 22, "E001", 14.5)
    e.ajouter_cours(Cours("Info", "M. Durand"))
    e.ajouter_cours(Cours("Maths", "Mme Martin"))
    assert len(e.liste_cours) == 2

def test_etudiant_str():
    e = Etudiant("Bob", 22, "E001", 14.5)
    e.ajouter_cours(Cours("Info", "M. Durand"))
    resultat = str(e)
    assert "Bob" in resultat
    assert "E001" in resultat
    assert "14.5" in resultat
    assert "Info" in resultat

def test_etudiant_repr():
    # Guide TP1 phase REFACTOR : __repr__ obligatoire
    e = Etudiant("Bob", 22, "E001", 14.5)
    r = repr(e)
    assert "Etudiant" in r
    assert "Bob" in r
    assert "E001" in r
