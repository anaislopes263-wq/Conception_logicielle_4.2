package com.ensta.gestion.modele;
import com.ensta.gestion.pattern.observer.EtudiantObserver;
import com.ensta.gestion.pattern.strategy.TriStrategy;
import com.ensta.gestion.pattern.strategy.TriParMoyenne;
import java.util.ArrayList;
import java.util.List;

/**
 * Hérite de Personne.
 * PATTERN 6 : OBSERVER (rôle Sujet / Observable)
 * Notifie ses observateurs à chaque ajout de note.
 * PATTERN 5 : STRATEGY
 * Délègue le calcul de mention à une stratégie interchangeable.
 */
public class Etudiant extends Personne {

    private String       numeroEtudiant;
    private double       moyenne;
    private List<Cours>  cours;
    private List<Double> notes;

    // PATTERN 5 : STRATEGY — stratégie de tri injectée dynamiquement
    private TriStrategy triStrategy;

    // PATTERN 6 : OBSERVER — liste des observateurs abonnés
    private final List<EtudiantObserver> observateurs = new ArrayList<>();

    // ------------------------------------------------------------------ //

    public Etudiant(String nom, int age, String numeroEtudiant) {
        super(nom, age);
        this.numeroEtudiant = numeroEtudiant;
        this.moyenne = 0.0;
        this.cours   = new ArrayList<>();
        this.notes   = new ArrayList<>();
        this.triStrategy = new TriParMoyenne(); // stratégie par défaut
    }

    // ------------------------------------------------------------------ //
    //  PATTERN 6 : OBSERVER
    // ------------------------------------------------------------------ //

    public void ajouterObservateur(EtudiantObserver obs) {
        observateurs.add(obs);
    }

    public void retirerObservateur(EtudiantObserver obs) {
        observateurs.remove(obs);
    }

    private void notifierObservateurs(double nouvelleNote) {
        for (EtudiantObserver obs : observateurs) {
            obs.notifierNouvelleNote(this, nouvelleNote);
        }
    }

    // ------------------------------------------------------------------ //
    //  Gestion des notes
    // ------------------------------------------------------------------ //

    public void ajouterNote(double note) {
        notes.add(note);
        recalculerMoyenne();
        notifierObservateurs(note); // 🔔 notification automatique
    }

    private void recalculerMoyenne() {
        moyenne = notes.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
    }

    // ------------------------------------------------------------------ //
    //  PATTERN 5 : STRATEGY — mention calculée via stratégie
    // ------------------------------------------------------------------ //

    /** Change la stratégie de tri dynamiquement (Pattern Strategy). */
    public void setTriStrategy(TriStrategy strategy) {
        this.triStrategy = strategy;
        System.out.println("[Strategy] Stratégie changée → " + strategy.getNom());
    }

    /** Calcule la mention selon la moyenne courante. */
    public String getMention() {
        if (moyenne >= 16) return "Très Bien";
        if (moyenne >= 14) return "Bien";
        if (moyenne >= 12) return "Assez Bien";
        if (moyenne >= 10) return "Passable";
        return "Insuffisant";
    }

    // ------------------------------------------------------------------ //
    //  Gestion des cours
    // ------------------------------------------------------------------ //

    public void ajouterCours(Cours c) { cours.add(c); }
    public List<Cours> getCours()     { return cours; }

    // ------------------------------------------------------------------ //
    //  Accesseurs
    // ------------------------------------------------------------------ //

    public String getNumeroEtudiant()          { return numeroEtudiant; }
    public double getMoyenne()                 { return moyenne; }
    public List<Double> getNotes()             { return notes; }
    public TriStrategy getTriStrategy()        { return triStrategy; }

    // ------------------------------------------------------------------ //

    @Override
    public String sePresenter() {
        return String.format("Étudiant[%s] %s (âge %d) — moyenne : %.2f — mention : %s",
                numeroEtudiant, getNom(), getAge(), moyenne, getMention());
    }
}