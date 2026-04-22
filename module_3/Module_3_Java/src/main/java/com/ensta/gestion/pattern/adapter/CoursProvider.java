package com.ensta.gestion.pattern.adapter;

import com.ensta.gestion.modele.Cours;

public interface CoursProvider {
    Cours getCours(int id);
}