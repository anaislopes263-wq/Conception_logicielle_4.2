package com.ensta.gestion.factory;

import com.ensta.gestion.modele.Etudiant;
import com.ensta.gestion.modele.Personne;
import com.ensta.gestion.modele.Enseignant;



/**
 * PATTERN 2 : FACTORY METHOD
 * Centralise la logique de création des Personne (Etudiant, Enseignant).
 * Le client n'utilise jamais directement "new Etudiant(...)" ou "new Enseignant(...)".
 *
 * Principe SOLID respecté :
 *  - Single Responsibility : la factory est seule responsable de l'instanciation.
 *  - Open/Closed : ajouter un nouveau type (ex. Administrateur) ne modifie pas
 *    les méthodes existantes.
 */
public class PersonneFactory {

    public enum TypePersonne { ETUDIANT, ENSEIGNANT }

    /**
     * Crée et retourne une Personne selon le type demandé.
     *
     * @param type            ETUDIANT ou ENSEIGNANT
     * @param nom             Nom de la personne
     * @param age             Âge de la personne
     * @param infoComplementaire  Numéro étudiant  OU  matière enseignée
     * @return instance de Etudiant ou Enseignant
     */
    public static Personne creer(TypePersonne type, String nom, int age,
                                 String infoComplementaire) {
        return switch (type) {
            case ETUDIANT   -> new Etudiant(nom, age, infoComplementaire);
            case ENSEIGNANT -> new Enseignant(nom, age, infoComplementaire);
        };
    }

    /** Raccourci pour créer un Etudiant directement typé. */
    public static Etudiant creerEtudiant(String nom, int age, String numero) {
        return (Etudiant) creer(TypePersonne.ETUDIANT, nom, age, numero);
    }

    /** Raccourci pour créer un Enseignant directement typé. */
    public static Enseignant creerEnseignant(String nom, int age, String matiere) {
        return (Enseignant) creer(TypePersonne.ENSEIGNANT, nom, age, matiere);
    }
}