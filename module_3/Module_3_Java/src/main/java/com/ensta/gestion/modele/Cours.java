package com.ensta.gestion.modele;
/**
 * Unité d'enseignement.
 */

public class Cours {

    private String nom;
    private String professeur;

    public Cours(String nom, String professeur) {
        this.nom = nom;
        this.professeur = professeur;
    }

    public String getNom()        { return nom; }
    public String getProfesseur() { return professeur; }

    @Override
    public String toString() {
        return "Cours{nom='" + nom + "', professeur='" + professeur + "'}";
    }
}