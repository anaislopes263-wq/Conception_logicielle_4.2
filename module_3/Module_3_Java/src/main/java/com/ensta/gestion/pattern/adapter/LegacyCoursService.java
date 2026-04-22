package com.ensta.gestion.pattern.adapter;

public class LegacyCoursService {

    public String getCoursData(int id) {
        return switch (id) {
            case 1 -> "Algorithmique;Dupont";
            case 2 -> "Architecture Logicielle;Martin";
            case 3 -> "Bases de Données;Bernard";
            default -> throw new IllegalArgumentException("Cours inconnu : " + id);
        };
    }
}