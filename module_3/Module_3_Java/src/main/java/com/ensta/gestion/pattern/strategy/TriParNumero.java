package com.ensta.gestion.pattern.strategy;

import com.ensta.gestion.modele.Etudiant;
import java.util.Comparator;
import java.util.List;

public class TriParNumero implements TriStrategy {

    @Override
    public void trier(List<Etudiant> etudiants) {
        etudiants.sort(Comparator.comparing(Etudiant::getNumeroEtudiant));
    }

    @Override
    public String getNom() { return "Tri par numéro étudiant"; }
}