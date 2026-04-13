public class TestEncapsulation {

    public static void main(String[] args) {

        Personne p = new Personne();

        // Test 1 : âge valide
        p.setAge(25);

        if (p.getAge() == 25) {
            System.out.println("Test age valide : OK");
        } else {
            System.out.println("Test age valide : ERREUR");
        }

        // Test 2 : âge invalide
        try {
            p.setAge(-5);
            System.out.println("Test age invalide : ERREUR (pas d'exception)");
        } catch (IllegalArgumentException e) {
            System.out.println("Test age invalide : OK (exception détectée)");
        }
    }
}