package com.ensta.gestion.pattern.decorator;

import com.ensta.gestion.modele.Etudiant;

public abstract class EtudiantDecorator extends Etudiant {

    protected final Etudiant etudiantDecore;

    public EtudiantDecorator(Etudiant etudiant) {
        super(etudiant.getNom(), etudiant.getAge(), etudiant.getNumeroEtudiant());
        this.etudiantDecore = etudiant;

        etudiant.getCours().forEach(this::ajouterCours);
        etudiant.getNotes().forEach(this::ajouterNote);
    }

    @Override
    public String sePresenter() {
        return etudiantDecore.sePresenter();
    }
}