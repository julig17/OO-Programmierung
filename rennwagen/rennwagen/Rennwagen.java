package rennwagen;

public class Rennwagen {

    // PRIVATE: Zugriff nur innerhalb dieser Klasse
    private String name;
    private String farbe;

    // PROTECTED: Zugriff innerhalb des Pakets
    // und in Unterklassen
    protected int leistungKW;
    protected double hubraum;

    // PUBLIC: Konstruktor
    public Rennwagen(String name, String farbe,
                     int leistungKW, double hubraum) {
        this.name = name;
        this.farbe = farbe;
        this.leistungKW = leistungKW;
        this.hubraum = hubraum;
    }

    // PUBLIC: Getter-Methoden
    public String getName() {
        return name;
    }

    public String getFarbe() {
        return farbe;
    }

    public int getLeistungKW() {
        return leistungKW;
    }

    public double getHubraum() {
        return hubraum;
    }

    // PUBLIC: Setter-Methoden mit Validierung
    public void setName(String name) {
        if (name != null && !name.isBlank()) {
            this.name = name;
        }
    }

    public void setFarbe(String farbe) {
        if (farbe != null && !farbe.isBlank()) {
            this.farbe = farbe;
        }
    }

    public void setLeistungKW(int leistungKW) {
        if (leistungKW > 0) {
            this.leistungKW = leistungKW;
        }
    }

    public void setHubraum(double hubraum) {
        if (hubraum > 0) {
            this.hubraum = hubraum;
        }
    }
}
