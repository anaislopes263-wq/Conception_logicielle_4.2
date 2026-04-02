public class Personne {
    private String nom;
    private int age;

    // Getters
    public String getNom() { return nom; }
    public int getAge() { return age; }

    // Setters
    public void setNom(String nom) { this.nom = nom; }
    public void setAge(int age) { 
        if (0 <= age && age <= 100) {
            this.age = age; 
        } else {
            throw new IllegalArgumentException("Age doit être entre 0 et 100");
        }
    }

    public void afficher_details(){
        System.out.println("Nom: " + nom);
        System.out.println("Age: " + age);
    }
}