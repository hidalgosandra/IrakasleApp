# irakaslea.py

class Irakaslea:
    def __init__(self, izena):
        self.izena = izena
        self.ordutegia = []  # Ordu okupatuak

    def gehitu_ordua(self, ordua):
        if ordua not in self.ordutegia:
            self.ordutegia.append(ordua)
            return True
        else: # Ordua gehituta dago
            return False

    def kendu_ordua(self, ordua):
        if ordua in self.ordutegia:
            self.ordutegia.remove(ordua)
            return True
        else: # Ordua ez dago
            return False

    def ordu_libreak(self):
        ordu_guztiak = [
            "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"
        ]
        ordu_libreak = []
        for ordua in ordu_guztiak:
            if ordua not in self.ordutegia:
                ordu_libreak.append(ordua)
        return ordu_libreak
