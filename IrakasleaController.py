import csv
from Irakaslea import Irakaslea

class IrakasleaController:
    def __init__(self, filename="irakasleak.csv"):
        self.filename = filename
        self.irakasleak = []

    def kargatu(self):
        self.irakasleak = []
        try:
            with open(self.filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    izen_abizena = row['izen_abizena']
                    ordutegia = row['ordutegia'].split(';') if row['ordutegia'] else []
                    irakaslea = Irakaslea(izen_abizena)
                    irakaslea.ordutegia = ordutegia
                    self.irakasleak.append(irakaslea)
        except FileNotFoundError:
            pass # Fitxategia ez dago, sortu berri bat

    def gorde(self):
        with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['izen_abizena', 'ordutegia']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for irakaslea in self.irakasleak:
                writer.writerow({
                    'izen_abizena': irakaslea.izen_abizena,
                    'ordutegia': ';'.join(irakaslea.ordutegia)
                })

    def irakasle_gehitu(self, izen_abizena):
        if any(i.izen_abizena == izen_abizena for i in self.irakasleak):
            return False
        berria = Irakaslea(izen_abizena)
        self.irakasleak.append(berria)
        return True

    def irakasle_kendu(self, izen_abizena):
        for i in self.irakasleak:
            if i.izen_abizena == izen_abizena:
                self.irakasleak.remove(i)
                return True
        return False
