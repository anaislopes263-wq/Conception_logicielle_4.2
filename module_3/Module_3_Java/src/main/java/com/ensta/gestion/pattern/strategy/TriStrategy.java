package com.ensta.gestion.pattern.strategy;

import com.ensta.gestion.modele.Etudiant;
import java.util.List;

public interface TriStrategy {
    void trier(List<Etudiant> etudiants);
    String getNom();
}