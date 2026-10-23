package rennwagen;
public class Main {
    public static void main(String[] args) {

        Rennwagen auto = new Rennwagen(
            "Lotus", "blau", 250, 4.0
        );

        // Zugriff über öffentliche Getter
        System.out.println(auto.getName());
        System.out.println(auto.getFarbe());

        // Änderung über öffentliche Setter
        auto.setFarbe("rot");

        System.out.println(auto.getFarbe());

        // Ungültiger Wert wird nicht übernommen
        auto.setLeistungKW(-100);

        System.out.println(auto.getLeistungKW());

        // Direkter Zugriff auf private Attribute:
        // auto.name = "Ferrari";  // Compilerfehler!
    }
}
