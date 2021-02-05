class Senf:

    def __init__(self, koernung, farbe, schaerfe, menge):
        self.koernung = koernung
        self.farbe = farbe
        self.schaerfe = schaerfe
        self.menge = menge

    def portion_senf(self, menge):
        print("Hier hast du deinen Senf!")
        self.menge -= menge


senf = Senf("grob", "dunkelgelb", "mittelscharf", 500)

print(senf.menge)

senf.portion_senf(50)

print(senf.menge)