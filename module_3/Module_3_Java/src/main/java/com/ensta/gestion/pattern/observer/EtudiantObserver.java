package com.ensta.gestion.pattern.observer;
import com.ensta.gestion.modele.Etudiant;
/**
 * PATTERN 6 : OBSERVER — Interface Observateur
 * Tout objet souhaitant être notifié des changements de note d'un Etudiant
 * doit implémenter cette interface.
 */
public interface EtudiantObserver {
    void notifierNouvelleNote(Etudiant etudiant, double nouvelleNote);
}