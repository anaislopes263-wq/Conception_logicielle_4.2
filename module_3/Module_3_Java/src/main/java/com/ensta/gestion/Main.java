package com.ensta.gestion;

import com.ensta.gestion.modele.Etudiant;
import com.ensta.gestion.modele.Enseignant;
import com.ensta.gestion.modele.Cours;
import com.ensta.gestion.factory.PersonneFactory;
import com.ensta.gestion.pattern.decorator.EtudiantBoursier;
import com.ensta.gestion.pattern.decorator.EtudiantDelegue;
import com.ensta.gestion.pattern.singleton.ScolariteManager;
import com.ensta.gestion.pattern.adapter.CoursAdapter;
import com.ensta.gestion.pattern.strategy.TriParMoyenne;
import com.ensta.gestion.pattern.strategy.TriParNom;
import com.ensta.gestion.pattern.adapter.LegacyCoursService;
import com.ensta.gestion.pattern.adapter.CoursProvider;


import java.util.List;

/**
 * Classe principale de démonstration.
 * Chaque section illustre un pattern distinct.
 */
public class Main {

    public static void main(String[] args) {

        separator("PATTERN 1 — SINGLETON : ScolariteManager");
        demoSingleton();

        separator("PATTERN 2 — FACTORY METHOD : PersonneFactory");
        demoFactory();

        separator("PATTERN 3 — DECORATOR : EtudiantBoursier / EtudiantDelegue");
        demoDecorator();

        separator("PATTERN 4 — ADAPTER : LegacyCours → Cours");
        demoAdapter();

        separator("PATTERN 5 — STRATEGY : Tri dynamique");
        demoStrategy();

        separator("PATTERN 6 — OBSERVER : Notification de notes");
        demoObserver();

        separator("STATISTIQUES GLOBALES FINALES");
        ScolariteManager.getInstance().afficherStatistiques();
    }

    // ------------------------------------------------------------------ //

    static void demoSingleton() {
        ScolariteManager m1 = ScolariteManager.getInstance();
        ScolariteManager m2 = ScolariteManager.getInstance();
        System.out.println("m1 == m2 ? " + (m1 == m2)); // doit afficher true
    }

    // ------------------------------------------------------------------ //

    static void demoFactory() {
        // Création via Factory — jamais de "new Etudiant(...)" côté client
        Etudiant alice = PersonneFactory.creerEtudiant("Alice", 20, "E001");
        Etudiant bob   = PersonneFactory.creerEtudiant("Bob",   22, "E002");
        Enseignant prof = PersonneFactory.creerEnseignant("M. Dupont", 45, "Algorithmique");

        System.out.println(alice.sePresenter());
        System.out.println(bob.sePresenter());
        System.out.println(prof.sePresenter());

        // Enregistrement dans le Singleton
        ScolariteManager.getInstance().ajouterEtudiant(alice);
        ScolariteManager.getInstance().ajouterEtudiant(bob);
    }

    // ------------------------------------------------------------------ //

    static void demoDecorator() {
        Etudiant charlie = PersonneFactory.creerEtudiant("Charlie", 21, "E003");
        charlie.ajouterNote(14.0);
        charlie.ajouterNote(16.0);

        // Décorer sans toucher à la classe Etudiant
        EtudiantBoursier boursier  = new EtudiantBoursier(charlie, 5000);
        EtudiantDelegue  delegue   = new EtudiantDelegue(boursier, "2026-INFO");

        // Cumul de décorateurs possible
        System.out.println("Simple   : " + charlie.sePresenter());
        System.out.println("Boursier : " + boursier.sePresenter());
        System.out.println("Délégué  : " + delegue.sePresenter());

        ScolariteManager.getInstance().ajouterEtudiant(charlie);
    }

    // ------------------------------------------------------------------ //

    static void demoAdapter() {
        LegacyCoursService legacy  = new LegacyCoursService();
        CoursProvider      adapter = new CoursAdapter(legacy);

        // Le client utilise CoursProvider — il ignore le format Legacy
        for (int id = 1; id <= 3; id++) {
            Cours c = adapter.getCours(id);
            System.out.println("Cours adapté : " + c);
        }

        // Ajout de ces cours à un étudiant existant
        Etudiant alice = ScolariteManager.getInstance().getEtudiants().get(0);
        alice.ajouterCours(adapter.getCours(1));
        alice.ajouterCours(adapter.getCours(2));
        System.out.println("Cours d'Alice : " + alice.getCours());
    }

    // ------------------------------------------------------------------ //

    static void demoStrategy() {
        List<Etudiant> liste = ScolariteManager.getInstance().getEtudiants();

        // On ajoute des notes pour avoir des moyennes variées
        liste.get(0).ajouterNote(12.0); // Alice
        liste.get(1).ajouterNote(17.0); // Bob

        Etudiant premier = liste.get(0);

        // Stratégie 1 : tri par moyenne (par défaut)
        premier.setTriStrategy(new TriParMoyenne());
        premier.getTriStrategy().trier(liste);
        System.out.println("Après tri par moyenne :");
        liste.forEach(e -> System.out.println("  " + e.getNom() + " → " + e.getMoyenne()));

        // Changement dynamique → tri par nom
        premier.setTriStrategy(new TriParNom());
        premier.getTriStrategy().trier(liste);
        System.out.println("Après tri par nom :");
        liste.forEach(e -> System.out.println("  " + e.getNom()));
    }

    // ------------------------------------------------------------------ //

    static void demoObserver() {
        // ScolariteManager est déjà abonné lors de ajouterEtudiant()
        // Chaque ajout de note déclenche automatiquement la notification
        Etudiant bob = ScolariteManager.getInstance().getEtudiants()
                .stream().filter(e -> e.getNom().equals("Bob"))
                .findFirst().orElseThrow();

        System.out.println("Ajout de notes à Bob → le ScolariteManager est notifié :");
        bob.ajouterNote(15.0);
        bob.ajouterNote(18.0);
    }

    // ------------------------------------------------------------------ //

    static void separator(String titre) {
        System.out.println("\n" + "─".repeat(60));
        System.out.println("  " + titre);
        System.out.println("─".repeat(60));
    }
}