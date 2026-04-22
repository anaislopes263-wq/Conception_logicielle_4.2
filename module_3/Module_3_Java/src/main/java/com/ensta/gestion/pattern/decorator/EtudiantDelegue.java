package com.ensta.gestion.pattern.decorator;

import com.ensta.gestion.modele.Etudiant;

public class EtudiantDelegue extends EtudiantDecorator {

    private String promotion;

    public EtudiantDelegue(Etudiant etudiant, String promotion) {
        super(etudiant);
        this.promotion = promotion;
    }

    public String getPromotion() { return promotion; }

    @Override
    public String sePresenter() {
        return super.sePresenter()
                + " | [DÉLÉGUÉ de la promotion " + promotion + "]";
    }
}