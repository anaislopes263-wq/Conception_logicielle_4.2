package com.ensta.gestion.modele;

public class Enseignant extends Personne {

    private String matiere;

    public Enseignant(String nom, int age, String matiere) {
        super(nom, age);
        this.matiere = matiere;
    }

    public String getMatiere() { return matiere; }

    @Override
    public String sePresenter() {
        return String.format("Enseignant %s (âge %d) — matière : %s",
                getNom(), getAge(), matiere);
    }
}