package com.ensta.gestion.modele;
/**
 * Classe abstraite de base.
 * Principe SOLID : Open/Closed — ouverte à l'extension (Etudiant, Enseignant),
 * fermée à la modification.
 */

public abstract class Personne {

    private String nom;
    private int age;

    public Personne(String nom, int age) {
        this.nom = nom;
        this.age = age;
    }

    public String getNom() { return nom; }
    public void   setNom(String nom) { this.nom = nom; }

    public int  getAge() { return age; }
    public void setAge(int age) { this.age = age; }

    /** Chaque sous-classe décrit sa présentation. */
    public abstract String sePresenter();

    @Override
    public String toString() { return sePresenter(); }
}