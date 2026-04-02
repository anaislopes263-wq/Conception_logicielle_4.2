import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        ArrayList<Personne> personnes = new ArrayList<>();

        // Etudiant
        Etudiant e1 = new Etudiant();
        e1.setNom("Alice");
        e1.setAge(20);
        e1.numeroEtudiant = "E123";
        e1.setMoyenne(15.5f);

        // Enseignant
        Enseignant prof = new Enseignant();
        prof.setNom("Dupont");
        prof.setAge(45);
        prof.salaire = 3000;

        // Etudiant
        Etudiant e2 = new Etudiant();
        e2.setNom("Bob");
        e2.setAge(22);
        e2.numeroEtudiant = "E456";
        e2.setMoyenne(16.0f);

        // Ajout
        personnes.add(e1);
        personnes.add(e2);
        personnes.add(prof);
        

        // Polymorphisme
        for (Personne p : personnes) {
            p.afficher_details();
            System.out.println("------------");
        }
    }
}