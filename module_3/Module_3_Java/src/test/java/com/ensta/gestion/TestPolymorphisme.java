import java.util.ArrayList;

public class TestPolymorphisme {

    public static void main(String[] args) {

        ArrayList<Personne> personnes = new ArrayList<>();

        Etudiant e = new Etudiant();
        e.setNom("Alice");
        e.setAge(20);
        e.setMoyenne(15.5f);

        Enseignant prof = new Enseignant();
        prof.setNom("Dupont");
        prof.setAge(45);
        prof.salaire = 3000;

        personnes.add(e);
        personnes.add(prof);

        // Test taille liste
        if (personnes.size() == 2) {
            System.out.println("Test liste : OK");
        } else {
            System.out.println("Test liste : ERREUR");
        }

        // Test types (polymorphisme)
        if (personnes.get(0) instanceof Etudiant &&
            personnes.get(1) instanceof Enseignant) {
            System.out.println("Test polymorphisme : OK");
        } else {
            System.out.println("Test polymorphisme : ERREUR");
        }

        // Test méthode commune (si elle existe)
        for (Personne p : personnes) {
            p.afficher_details();
            System.out.println("-----");
        }
    }
}