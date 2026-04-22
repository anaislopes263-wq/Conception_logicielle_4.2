package com.ensta.gestion.pattern.strategy;

import com.ensta.gestion.modele.Etudiant;
import java.util.Comparator;
import java.util.List;

public class TriParMoyenne implements TriStrategy {

    @Override
    public void trier(List<Etudiant> etudiants) {
        etudiants.sort(Comparator.comparingDouble(Etudiant::getMoyenne).reversed());
    }

    @Override
    public String getNom() { return "Tri par moyenne (décroissant)"; }
}