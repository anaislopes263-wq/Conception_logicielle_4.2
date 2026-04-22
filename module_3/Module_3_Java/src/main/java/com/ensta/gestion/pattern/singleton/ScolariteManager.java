package com.ensta.gestion.pattern.singleton;

import com.ensta.gestion.modele.Etudiant;
import com.ensta.gestion.pattern.observer.EtudiantObserver;
import java.util.ArrayList;

import java.util.List;

/**
 * PATTERN 1 : SINGLETON
 * Une seule instance globale qui centralise la liste de tous les étudiants.
 * PATTERN 6 : OBSERVER (rôle Observateur)
 * Reçoit les notifications quand une note est ajoutée à un étudiant.
 */
public class ScolariteManager implements EtudiantObserver {

    // Instance unique (volatile pour la thread-safety)
    private static volatile ScolariteManager instance;

    private final List<Etudiant> etudiants = new ArrayList<>();

    // Statistiques globales mises à jour via Observer
    private double moyenneGlobale = 0.0;

    // Constructeur privé → empêche toute instanciation externe
    private ScolariteManager() {}

    /** Point d'accès unique à l'instance (Double-Checked Locking). */
    public static ScolariteManager getInstance() {
        if (instance == null) {
            synchronized (ScolariteManager.class) {
                if (instance == null) {
                    instance = new ScolariteManager();
                }
            }
        }
        return instance;
    }

    // ------------------------------------------------------------------ //
    //  Gestion des étudiants
    // ------------------------------------------------------------------ //

    public void ajouterEtudiant(Etudiant e) {
        etudiants.add(e);
        e.ajouterObservateur(this);   // le manager s'abonne automatiquement
        recalculerMoyenneGlobale();
        System.out.println("[ScolariteManager] Étudiant ajouté : " + e.getNom());
    }

    public List<Etudiant> getEtudiants() {
        return etudiants;
    }

    // ------------------------------------------------------------------ //
    //  PATTERN 6 : OBSERVER — callback déclenché par Etudiant
    // ------------------------------------------------------------------ //

    @Override
    public void notifierNouvelleNote(Etudiant etudiant, double nouvelleNote) {
        System.out.println("[ScolariteManager] Notification : "
                + etudiant.getNom() + " a reçu la note " + nouvelleNote
                + " → nouvelle moyenne : " + etudiant.getMoyenne());
        recalculerMoyenneGlobale();
    }

    // ------------------------------------------------------------------ //
    //  Statistiques
    // ------------------------------------------------------------------ //

    private void recalculerMoyenneGlobale() {
        if (etudiants.isEmpty()) { moyenneGlobale = 0.0; return; }
        moyenneGlobale = etudiants.stream()
                .mapToDouble(Etudiant::getMoyenne)
                .average()
                .orElse(0.0);
    }

    public double getMoyenneGlobale() { return moyenneGlobale; }

    public void afficherStatistiques() {
        System.out.println("\n=== Statistiques ScolariteManager ===");
        System.out.println("Nombre d'étudiants : " + etudiants.size());
        System.out.printf("Moyenne globale    : %.2f%n", moyenneGlobale);
        System.out.println("=====================================\n");
    }
}