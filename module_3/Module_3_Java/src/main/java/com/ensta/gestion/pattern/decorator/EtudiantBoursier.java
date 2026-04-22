package com.ensta.gestion.pattern.decorator;

import com.ensta.gestion.modele.Etudiant;

public class EtudiantBoursier extends EtudiantDecorator {

    private double montantBourse;

    public EtudiantBoursier(Etudiant etudiant, double montantBourse) {
        super(etudiant);
        this.montantBourse = montantBourse;
    }

    public double getMontantBourse() { return montantBourse; }

    @Override
    public String sePresenter() {
        return super.sePresenter()
                + String.format(" | [BOURSIER — bourse : %.0f €]", montantBourse);
    }
}