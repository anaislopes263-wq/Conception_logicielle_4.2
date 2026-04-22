package com.ensta.gestion.pattern.adapter;

import com.ensta.gestion.modele.Cours;

public class CoursAdapter implements CoursProvider {

    private final LegacyCoursService legacyService;

    public CoursAdapter(LegacyCoursService legacyService) {
        this.legacyService = legacyService;
    }

    @Override
    public Cours getCours(int id) {
        String data    = legacyService.getCoursData(id);
        String[] parts = data.split(";");

        if (parts.length != 2) {
            throw new IllegalArgumentException(
                    "Format Legacy invalide : '" + data + "'");
        }

        return new Cours(parts[0].trim(), parts[1].trim());
    }
}