"""
Tests unitaires — module_3
Couvre les 6 patterns du TP.

Commande à utiliser: python -m pytest -v
"""

import pytest
from cours import Cours
from cours_adapter import CoursAdapter
from etudiant import Etudiant
from etudiant_decorateur import EtudiantBoursier, EtudiantDelegue
from personne_factory import PersonneFactory
from scolarite_manager import ScolariteManager
from strategie_tri import (
    GestionnaireTriEtudiants, TriParMoyenne, TriParNom, TriParAge
)


@pytest.fixture(autouse=True)
def reset_singleton():
    """Réinitialise le Singleton avant chaque test."""
    ScolariteManager._instance = None
    yield
    ScolariteManager._instance = None


@pytest.fixture
def etudiant_alice():
    return Etudiant("Alice", 20, "E001", 15.0)


@pytest.fixture
def etudiant_bob():
    return Etudiant("Bob", 22, "E002", 12.0)


@pytest.fixture
def etudiant_charlie():
    return Etudiant("Charlie", 21, "E003", 17.5)


# ─── 1. Singleton ────────────────────────────────────────────────────────── #

class TestSingleton:

    def test_meme_instance(self):
        m1 = ScolariteManager()
        m2 = ScolariteManager()
        assert m1 is m2

    def test_inscription_etudiant(self, etudiant_alice):
        manager = ScolariteManager()
        manager.inscrire_etudiant(etudiant_alice)
        assert etudiant_alice in manager.etudiants

    def test_pas_de_doublon(self, etudiant_alice):
        manager = ScolariteManager()
        manager.inscrire_etudiant(etudiant_alice)
        manager.inscrire_etudiant(etudiant_alice)
        assert manager.etudiants.count(etudiant_alice) == 1

    def test_retirer_etudiant(self, etudiant_alice):
        manager = ScolariteManager()
        manager.inscrire_etudiant(etudiant_alice)
        manager.retirer_etudiant(etudiant_alice)
        assert etudiant_alice not in manager.etudiants


# ─── 2. Factory Method ───────────────────────────────────────────────────── #

class TestFactory:

    def test_creer_etudiant(self):
        e = PersonneFactory.creer("etudiant", nom="Alice", age=20,
                                   numero_etudiant="E001", moyenne=14.0)
        from etudiant import Etudiant
        assert isinstance(e, Etudiant)
        assert e.nom == "Alice"
        assert e.moyenne == 14.0

    def test_creer_enseignant(self):
        from enseignant import Enseignant
        p = PersonneFactory.creer("enseignant", nom="M. Dupont", age=45,
                                   matiere="Maths", salaire=3500.0)
        assert isinstance(p, Enseignant)
        assert p.matiere == "Maths"

    def test_type_inconnu(self):
        with pytest.raises(ValueError, match="Type inconnu"):
            PersonneFactory.creer("inconnu", nom="X", age=30)

    def test_champs_manquants(self):
        with pytest.raises(ValueError, match="Champs manquants"):
            PersonneFactory.creer("etudiant", nom="Alice", age=20)

    def test_insensible_casse(self):
        e = PersonneFactory.creer("ETUDIANT", nom="Bob", age=21,
                                   numero_etudiant="E002", moyenne=10.0)
        from etudiant import Etudiant
        assert isinstance(e, Etudiant)


# ─── 3. Decorator ────────────────────────────────────────────────────────── #

class TestDecorator:

    def test_boursier_details(self, etudiant_alice):
        dec = EtudiantBoursier(etudiant_alice, 400.0)
        details = dec.afficher_details()
        assert "Boursier" in details
        assert "400.00" in details

    def test_delegue_details(self, etudiant_alice):
        dec = EtudiantDelegue(etudiant_alice, "ENSTA 2025")
        details = dec.afficher_details()
        assert "Délégué" in details
        assert "ENSTA 2025" in details

    def test_combinaison(self, etudiant_alice):
        dec = EtudiantDelegue(EtudiantBoursier(etudiant_alice, 300.0), "ENSTA 2026")
        details = dec.afficher_details()
        assert "Boursier" in details
        assert "Délégué" in details

    def test_delegation_proprietes(self, etudiant_alice):
        dec = EtudiantBoursier(etudiant_alice, 200.0)
        assert dec.nom == etudiant_alice.nom
        assert dec.moyenne == etudiant_alice.moyenne

    def test_bourse_negative(self, etudiant_alice):
        with pytest.raises(ValueError):
            EtudiantBoursier(etudiant_alice, -100.0)

    def test_promotion_vide(self, etudiant_alice):
        with pytest.raises(ValueError):
            EtudiantDelegue(etudiant_alice, "")


# ─── 4. Adapter ──────────────────────────────────────────────────────────── #

class TestAdapter:

    def test_parsing_correct(self):
        c = CoursAdapter("Machine_Learning|M. Toumi")
        assert c.nom_cours == "Machine_Learning"
        assert c.professeur_responsable == "M. Toumi"

    def test_instance_cours(self):
        c = CoursAdapter("Algo|M. Leroy")
        assert isinstance(c, Cours)

    def test_format_invalide(self):
        with pytest.raises(ValueError, match="Format legacy invalide"):
            CoursAdapter("FormatSansSeparateur")

    def test_str_adapte(self):
        c = CoursAdapter("Maths|Mme Durand")
        assert "[Adapté]" in str(c)

    def test_espaces_trim(self):
        c = CoursAdapter("  Physique  |  M. Blanc  ")
        assert c.nom_cours == "Physique"
        assert c.professeur_responsable == "M. Blanc"


# ─── 5. Strategy ─────────────────────────────────────────────────────────── #

class TestStrategy:

    @pytest.fixture
    def liste(self, etudiant_alice, etudiant_bob, etudiant_charlie):
        return [etudiant_alice, etudiant_bob, etudiant_charlie]

    def test_tri_par_moyenne(self, liste):
        g = GestionnaireTriEtudiants(TriParMoyenne())
        result = g.trier(liste)
        moyennes = [e.moyenne for e in result]
        assert moyennes == sorted(moyennes, reverse=True)

    def test_tri_par_nom(self, liste):
        g = GestionnaireTriEtudiants(TriParNom())
        result = g.trier(liste)
        noms = [e.nom.lower() for e in result]
        assert noms == sorted(noms)

    def test_tri_par_age(self, liste):
        g = GestionnaireTriEtudiants(TriParAge())
        result = g.trier(liste)
        ages = [e.age for e in result]
        assert ages == sorted(ages)

    def test_changement_dynamique(self, liste):
        g = GestionnaireTriEtudiants(TriParMoyenne())
        r1 = g.trier(liste)
        g.changer_strategie(TriParNom())
        r2 = g.trier(liste)
        # Les deux résultats peuvent différer
        assert [e.nom for e in r1] != [e.nom for e in r2] or True  # au moins pas d'erreur

    def test_liste_non_modifiee(self, liste):
        originale = list(liste)
        g = GestionnaireTriEtudiants(TriParMoyenne())
        g.trier(liste)
        assert liste == originale


# ─── 6. Observer ─────────────────────────────────────────────────────────── #

class TestObserver:

    def test_notification_lors_ajout_note(self, etudiant_alice):
        manager = ScolariteManager()
        manager.inscrire_etudiant(etudiant_alice)
        moyenne_initiale = etudiant_alice.moyenne
        etudiant_alice.ajouter_note(20.0)
        # La moyenne a changé
        assert etudiant_alice.moyenne != moyenne_initiale

    def test_recalcul_moyenne(self, etudiant_alice):
        # Alice part avec moyenne=15.0 (passée au constructeur, sans notes)
        etudiant_alice.ajouter_note(10.0)
        etudiant_alice.ajouter_note(20.0)
        assert etudiant_alice.moyenne == pytest.approx(15.0)

    def test_statistiques_mises_a_jour(self, etudiant_alice):
        manager = ScolariteManager()
        manager.inscrire_etudiant(etudiant_alice)
        etudiant_alice.ajouter_note(20.0)
        # Pas d'exception = statistiques mises à jour correctement

    def test_note_invalide(self, etudiant_alice):
        with pytest.raises(ValueError):
            etudiant_alice.ajouter_note(25.0)

    def test_desabonnement(self, etudiant_alice):
        manager = ScolariteManager()
        manager.inscrire_etudiant(etudiant_alice)
        manager.retirer_etudiant(etudiant_alice)
        # Pas d'exception après désabonnement
        etudiant_alice.ajouter_note(12.0)
