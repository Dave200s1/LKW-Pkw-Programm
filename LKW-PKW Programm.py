class Farhzeug():

    def __init__(self, farbe, baujahr, kmstand, sitze, marke):
        """ Eigenschaften farbe, baujahr, kmstand, Sitzplätze, Marke erfassen """
        self.farbe   = farbe
        self.baujahr = baujahr
        self.kmstand = kmstand
        self.sitze   = sitze
        self.marke   = marke

    def hupen(self):
        
        print("Trööt")

    def fahren(self, km):
        self.kmstand += km
        print("Ich fahre ", km, " Kilometer")
        print("Insgesamt bin ich ", self.kmstand ," gefahren")

    def parken(self):
       
        print("Ich habe eine Parkplatz gefunden")

    def kilometerstand(self):
        """ Ausgabe des KM-Standes vom Tacho """
        print("Ich habe ", str(self.kmstand) ," auf dem Tacho")
#GeschwisterKlassen PKW und LKW unten
class PKW(Farhzeug):
    def __init__(self,farbe,baujahr,kmstand,sitze,marke,kofferraum):
        self.kofferraum=kofferraum
        super().__init__(farbe,baujahr,kmstand,sitze,marke)


class LKW(Farhzeug):
    def __init__(self,farbe,baujahr,kmstand,sitze,marke):
        super().__init__(farbe,baujahr,kmstand,sitze,marke)

    def parken(self):
        print("auf Firmenhof abgestellt")

    def aufladen(self,menge):
        print(menge,"Paletten werden aufgeladen")



trabi = PKW("rot", 1981, 143000, 4, "Trabi",20)
trabi.hupen()
trabi.kilometerstand()
trabi.fahren(5)
trabi.parken()
print(trabi.kofferraum)
print("\n")

Man= LKW("blau",2008,34800,2,"Man")
Man.parken()
Man.aufladen(3)