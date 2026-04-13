import java.util.ArrayList;

public class Etudiant extends Personne {

    public String numeroEtudiant;
    private float moyenne;
    public String filiere;
    public ArrayList<String> coursSuivis;

    // Getters
    public float getMoyenne() { return moyenne; }

    // Setters
    public void setMoyenne(float moyenne) {
        if(moyenne >= 0.0f && moyenne <= 20.0f) {
            this.moyenne = moyenne;
        } else {
            throw new IllegalArgumentException("Moyenne doit être entre 0.0 et 20.0");
        }
     }
     @Override
     public void afficher_details() {
         super.afficher_details(); // affiche nom + age
        System.out.println("Moyenne: " + getMoyenne());
     }
}