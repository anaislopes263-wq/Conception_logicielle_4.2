@startuml
title Diagramme de Séquence — Système de Gestion des Étudiants

actor Utilisateur
participant "Main" as Main
participant "Etudiant\n(anais)" as Etudiant
participant "Cours\n(TDE)" as Cours1
participant "Cours\n(ML)" as Cours2
participant "afficher_details()\n(service d'affichage)" as Affichage

== Création de l'étudiant ==
Utilisateur -> Main : exécuter()
Main -> Etudiant : Etudiant("anais", 21, "E001", 15.5)
activate Etudiant
Etudiant --> Main : anais

== Création des cours ==
Main -> Cours1 : Cours("Décision_estimation", "Mme Quidu")
activate Cours1
Cours1 --> Main : TDE

Main -> Cours2 : Cours("Machine_Learning", "M. Toumi")
activate Cours2
Cours2 --> Main : ML

== Assignation des cours à l'étudiant ==
Main -> Etudiant : ajouter_cours(TDE)
Etudiant -> Etudiant : __liste_cours.append(TDE)
Etudiant --> Main : OK

Main -> Etudiant : ajouter_cours(ML)
Etudiant -> Etudiant : __liste_cours.append(ML)
Etudiant --> Main : OK

== Génération du rapport (affichage) ==
Main -> Affichage : afficher_details(anais)
activate Affichage
Affichage -> Etudiant : afficher_details()
Etudiant -> Etudiant : super().afficher_details()
Etudiant -> Etudiant : [c.nom_cours for c in __liste_cours]
Etudiant --> Affichage : rapport formaté (nom, âge, moyenne, cours)
Affichage --> Main : affiche le rapport
deactivate Affichage

deactivate Cours1
deactivate Cours2
deactivate Etudiant
@enduml