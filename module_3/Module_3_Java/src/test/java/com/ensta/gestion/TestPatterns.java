package com.ensta.gestion;

import com.ensta.gestion.modele.Etudiant;
import com.ensta.gestion.modele.Enseignant;
import com.ensta.gestion.modele.Cours;
import com.ensta.gestion.factory.PersonneFactory;
import com.ensta.gestion.pattern.singleton.ScolariteManager;
import com.ensta.gestion.pattern.decorator.EtudiantBoursier;
import com.ensta.gestion.pattern.decorator.EtudiantDelegue;
import com.ensta.gestion.pattern.adapter.CoursAdapter;
import com.ensta.gestion.pattern.adapter.CoursProvider;
import com.ensta.gestion.pattern.adapter.LegacyCoursService;
import com.ensta.gestion.pattern.strategy.TriParMoyenne;
import com.ensta.gestion.pattern.strategy.TriParNom;
import com.ensta.gestion.pattern.observer.EtudiantObserver;

import java.util.ArrayList;
import java.util.List;

/**
 * Tests manuels des 6 patterns.
 * Chaque test affiche PASS ou FAIL avec un message explicite.
 */
public class TestPatterns {

    static int passed = 0;
    static int failed = 0;

    public static void main(String[] args) {

        separator("PATTERN 1 — SINGLETON");
        testSingleton_memeInstance();
        testSingleton_etatPartage();

        separator("PATTERN 2 — FACTORY METHOD");
        testFactory_creerEtudiant();
        testFactory_creerEnseignant();
        testFactory_typesDistincts();

        separator("PATTERN 3 — DECORATOR");
        testDecorator_boursierAffichage();
        testDecorator_delegueAffichage();
        testDecorator_cumul();
        testDecorator_moyenneIntacte();

        separator("PATTERN 4 — ADAPTER");
        testAdapter_coursValide();
        testAdapter_tousLesCours();
        testAdapter_idInconnu();

        separator("PATTERN 5 — STRATEGY");
        testStrategy_triParMoyenne();
        testStrategy_triParNom();
        testStrategy_changementDynamique();

        separator("PATTERN 6 — OBSERVER");
        testObserver_notificationNote();
        testObserver_moyenneGlobaleMiseAJour();

        separator("RÉSULTAT FINAL");
        System.out.println("  PASS : " + passed);
        System.out.println("  FAIL : " + failed);
        System.out.println("  TOTAL : " + (passed + failed));
    }

    // ================================================================== //
    //  PATTERN 1 — SINGLETON
    // ================================================================== //

    static void testSingleton_memeInstance() {
        ScolariteManager m1 = ScolariteManager.getInstance();
        ScolariteManager m2 = ScolariteManager.getInstance();
        assertTrue("Singleton : m1 et m2 sont la même instance", m1 == m2);
    }

    static void testSingleton_etatPartage() {
        ScolariteManager manager = ScolariteManager.getInstance();
        int avant = manager.getEtudiants().size();
        Etudiant e = PersonneFactory.creerEtudiant("TestSingleton", 20, "T001");
        manager.ajouterEtudiant(e);
        int apres = ScolariteManager.getInstance().getEtudiants().size();
        assertTrue("Singleton : état partagé entre les deux références", apres == avant + 1);
    }

    // ================================================================== //
    //  PATTERN 2 — FACTORY METHOD
    // ================================================================== //

    static void testFactory_creerEtudiant() {
        Etudiant e = PersonneFactory.creerEtudiant("Alice", 20, "E001");
        assertTrue("Factory : creerEtudiant retourne un Etudiant non null", e != null);
        assertTrue("Factory : nom correct", e.getNom().equals("Alice"));
        assertTrue("Factory : numéro correct", e.getNumeroEtudiant().equals("E001"));
    }

    static void testFactory_creerEnseignant() {
        Enseignant prof = PersonneFactory.creerEnseignant("M. Dupont", 45, "Maths");
        assertTrue("Factory : creerEnseignant retourne un Enseignant non null", prof != null);
        assertTrue("Factory : matière correcte", prof.getMatiere().equals("Maths"));
    }

    static void testFactory_typesDistincts() {
        Etudiant e   = PersonneFactory.creerEtudiant("Bob", 22, "E002");
        Enseignant p = PersonneFactory.creerEnseignant("Prof", 40, "Info");

        assertTrue("Factory : Etudiant instanceof Etudiant",     e instanceof Etudiant);
        assertTrue("Factory : Enseignant instanceof Enseignant", p instanceof Enseignant);
        assertTrue("Factory : classes différentes",
            !e.getClass().equals(p.getClass()));
}

    // ================================================================== //
    //  PATTERN 3 — DECORATOR
    // ================================================================== //

    static void testDecorator_boursierAffichage() {
        Etudiant e = PersonneFactory.creerEtudiant("Clara", 21, "E010");
        EtudiantBoursier b = new EtudiantBoursier(e, 3000);
        assertTrue("Decorator : affichage contient BOURSIER",
                b.sePresenter().contains("BOURSIER"));
        assertTrue("Decorator : affichage contient le montant",
                b.sePresenter().contains("3000"));
    }

    static void testDecorator_delegueAffichage() {
        Etudiant e = PersonneFactory.creerEtudiant("David", 22, "E011");
        EtudiantDelegue d = new EtudiantDelegue(e, "2026-INFO");
        assertTrue("Decorator : affichage contient DÉLÉGUÉ",
                d.sePresenter().contains("DÉLÉGUÉ"));
        assertTrue("Decorator : affichage contient la promotion",
                d.sePresenter().contains("2026-INFO"));
    }

    static void testDecorator_cumul() {
        Etudiant e = PersonneFactory.creerEtudiant("Eva", 20, "E012");
        EtudiantBoursier b = new EtudiantBoursier(e, 5000);
        EtudiantDelegue  d = new EtudiantDelegue(b, "2026-MECA");
        assertTrue("Decorator : cumul contient BOURSIER",  d.sePresenter().contains("BOURSIER"));
        assertTrue("Decorator : cumul contient DÉLÉGUÉ",   d.sePresenter().contains("DÉLÉGUÉ"));
    }

    static void testDecorator_moyenneIntacte() {
        Etudiant e = PersonneFactory.creerEtudiant("Frank", 21, "E013");
        e.ajouterNote(14.0);
        e.ajouterNote(16.0);
        EtudiantBoursier b = new EtudiantBoursier(e, 2000);
        assertTrue("Decorator : la moyenne de l'étudiant décoré est préservée",
                b.getMoyenne() >= 14.0);
    }

    // ================================================================== //
    //  PATTERN 4 — ADAPTER
    // ================================================================== //

    static void testAdapter_coursValide() {
        CoursProvider adapter = new CoursAdapter(new LegacyCoursService());
        Cours c = adapter.getCours(1);
        assertTrue("Adapter : cours non null", c != null);
        assertTrue("Adapter : nom du cours correct",
                c.getNom().equals("Algorithmique"));
        assertTrue("Adapter : professeur correct",
                c.getProfesseur().equals("Dupont"));
    }

    static void testAdapter_tousLesCours() {
        CoursProvider adapter = new CoursAdapter(new LegacyCoursService());
        boolean ok = true;
        for (int i = 1; i <= 3; i++) {
            Cours c = adapter.getCours(i);
            if (c == null || c.getNom().isEmpty()) { ok = false; break; }
        }
        assertTrue("Adapter : les 3 cours legacy sont bien adaptés", ok);
    }

    static void testAdapter_idInconnu() {
        CoursProvider adapter = new CoursAdapter(new LegacyCoursService());
        boolean exceptionLevee = false;
        try {
            adapter.getCours(99);
        } catch (IllegalArgumentException e) {
            exceptionLevee = true;
        }
        assertTrue("Adapter : exception levée pour id inconnu", exceptionLevee);
    }

    // ================================================================== //
    //  PATTERN 5 — STRATEGY
    // ================================================================== //

    static void testStrategy_triParMoyenne() {
        List<Etudiant> liste = creerListeTest();
        new TriParMoyenne().trier(liste);
        assertTrue("Strategy : tri par moyenne — premier a la moyenne la plus haute",
                liste.get(0).getMoyenne() >= liste.get(1).getMoyenne());
    }

    static void testStrategy_triParNom() {
        List<Etudiant> liste = creerListeTest();
        new TriParNom().trier(liste);
        assertTrue("Strategy : tri par nom — ordre alphabétique respecté",
                liste.get(0).getNom().compareTo(liste.get(1).getNom()) <= 0);
    }

    static void testStrategy_changementDynamique() {
    Etudiant e = PersonneFactory.creerEtudiant("Test", 20, "T999");
    e.setTriStrategy(new TriParMoyenne());
    assertTrue("Strategy : stratégie TriParMoyenne assignée",
            e.getTriStrategy().getClass().equals(TriParMoyenne.class));
    e.setTriStrategy(new TriParNom());
    assertTrue("Strategy : stratégie changée dynamiquement en TriParNom",
            e.getTriStrategy().getClass().equals(TriParNom.class));
}

    // ================================================================== //
    //  PATTERN 6 — OBSERVER
    // ================================================================== //

    static void testObserver_notificationNote() {
        Etudiant e = PersonneFactory.creerEtudiant("Obs", 20, "O001");

        // Observateur maison qui comptabilise les notifications reçues
        List<Double> notesRecues = new ArrayList<>();
        e.ajouterObservateur((etudiant, note) -> notesRecues.add(note));

        e.ajouterNote(12.0);
        e.ajouterNote(15.0);

        assertTrue("Observer : 2 notifications reçues", notesRecues.size() == 2);
        assertTrue("Observer : première note notifiée = 12.0", notesRecues.get(0) == 12.0);
        assertTrue("Observer : deuxième note notifiée = 15.0", notesRecues.get(1) == 15.0);
    }

    static void testObserver_moyenneGlobaleMiseAJour() {
        ScolariteManager manager = ScolariteManager.getInstance();
        Etudiant e = PersonneFactory.creerEtudiant("ObsGlobal", 20, "O002");
        manager.ajouterEtudiant(e);
        double avant = manager.getMoyenneGlobale();
        e.ajouterNote(20.0); // note maximale → doit faire monter la moyenne
        assertTrue("Observer : moyenne globale mise à jour après ajout de note",
                manager.getMoyenneGlobale() >= avant);
    }

    // ================================================================== //
    //  UTILITAIRES
    // ================================================================== //

    static List<Etudiant> creerListeTest() {
        Etudiant z = PersonneFactory.creerEtudiant("Zoe",   20, "X001");
        Etudiant a = PersonneFactory.creerEtudiant("Alice", 21, "X002");
        Etudiant m = PersonneFactory.creerEtudiant("Marc",  22, "X003");
        z.ajouterNote(10.0);
        a.ajouterNote(18.0);
        m.ajouterNote(14.0);
        List<Etudiant> liste = new ArrayList<>();
        liste.add(z); liste.add(a); liste.add(m);
        return liste;
    }

    static void assertTrue(String message, boolean condition) {
        if (condition) {
            System.out.println(" PASS — " + message);
            passed++;
        } else {
            System.out.println(" FAIL — " + message);
            failed++;
        }
    }

    static void assertFalse(String message, boolean condition) {
        assertTrue(message, !condition);
    }

    static void separator(String titre) {
        System.out.println("\n" + "─".repeat(60));
        System.out.println("  " + titre);
        System.out.println("─".repeat(60));
    }
}