"""
TP2 - Tests d'encapsulation
On vérifie que les données sont bien protégées avec des règles de validation.
"""
import pytest
from personne import Personne
from etudiant import Etudiant


# Tests de validation de l'âge (classe Personne)

def test_age_valide():
    p = Personne("Alice", 20)
    assert p.age == 20

def test_age_negatif_interdit():
    with pytest.raises(ValueError):
        Personne("Alice", -1)

def test_age_zero_interdit():
    with pytest.raises(ValueError):
        Personne("Alice", 0)

def test_age_100_interdit():
    with pytest.raises(ValueError):
        Personne("Alice", 100)

def test_age_99_autorise():
    p = Personne("Alice", 99)
    assert p.age == 99

def test_modifier_age_valide():
    p = Personne("Alice", 20)
    p.age = 25
    assert p.age == 25

def test_modifier_age_invalide():
    p = Personne("Alice", 20)
    with pytest.raises(ValueError):
        p.age = -5


# Tests de validation du nom (classe Personne)

def test_nom_vide_interdit():
    with pytest.raises(ValueError):
        Personne("", 20)

def test_nom_espaces_interdit():
    with pytest.raises(ValueError):
        Personne("   ", 20)


# Tests de validation de la moyenne (classe Etudiant)

def test_moyenne_valide():
    e = Etudiant("Bob", 22, "E001", 14.5)
    assert e.moyenne == 14.5

def test_moyenne_negative_interdite():
    with pytest.raises(ValueError):
        Etudiant("Bob", 22, "E001", -1)

def test_moyenne_trop_grande_interdite():
    with pytest.raises(ValueError):
        Etudiant("Bob", 22, "E001", 21)

def test_moyenne_zero_autorisee():
    e = Etudiant("Bob", 22, "E001", 0)
    assert e.moyenne == 0

def test_moyenne_20_autorisee():
    e = Etudiant("Bob", 22, "E001", 20)
    assert e.moyenne == 20

def test_modifier_moyenne_invalide():
    e = Etudiant("Bob", 22, "E001", 14.5)
    with pytest.raises(ValueError):
        e.moyenne = 25


# Test : numéro étudiant en lecture seule
def test_numero_etudiant_lecture_seule():
    e = Etudiant("Bob", 22, "E001", 14.5)
    with pytest.raises(AttributeError):
        e.numero_etudiant = "E999"


# Test : liste_cours accessible uniquement via ajouter_cours()
def test_liste_cours_non_modifiable_directement():
    from cours import Cours
    e = Etudiant("Bob", 22, "E001", 14.5)
    # La propriété retourne une copie : modifier la copie ne change rien
    copie = e.liste_cours
    copie.append(Cours("Hack", "Inconnu"))
    assert len(e.liste_cours) == 0   # la vraie liste interne est intacte

def test_liste_cours_via_ajouter_cours():
    from cours import Cours
    e = Etudiant("Bob", 22, "E001", 14.5)
    e.ajouter_cours(Cours("Info", "M. Durand"))
    assert len(e.liste_cours) == 1
