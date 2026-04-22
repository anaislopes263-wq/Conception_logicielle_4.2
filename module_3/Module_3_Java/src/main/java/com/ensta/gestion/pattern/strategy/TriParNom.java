package com.ensta.gestion.pattern.strategy;

import com.ensta.gestion.modele.Etudiant;
import java.util.Comparator;
import java.util.List;

public class TriParNom implements TriStrategy {

    @Override
    public void trier(List<Etudiant> etudiants) {
        etudiants.sort(Comparator.comparing(Etudiant::getNom));
    }

    @Override
    public String getNom() { return "Tri par nom (alphabétique)"; }
}