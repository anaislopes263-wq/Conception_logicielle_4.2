

public class Enseignant extends Personne {
    public int salaire;

    @Override
    public void afficher_details() {
        super.afficher_details(); // affiche nom + age
        System.out.println("Salaire: " + salaire);
    }
}