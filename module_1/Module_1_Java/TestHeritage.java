public class TestHeritage {

    public static void main(String[] args) {

        Etudiant e = new Etudiant();
        e.setNom("Alice");
        e.setAge(20);

        if (e instanceof Personne) {
            System.out.println("Test héritage : OK (Etudiant hérite de Personne)");
        } else {
            System.out.println("Test héritage : ERREUR");
        }

        if (e.getNom().equals("Alice") && e.getAge() == 20) {
            System.out.println("Test getters : OK");
        } else {
            System.out.println("Test getters : ERREUR");
        }
    }
}