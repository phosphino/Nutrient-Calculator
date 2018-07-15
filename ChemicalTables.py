import csv
from collections import namedtuple


class Ions:
    def __init__(self, iontable = 'IonTable.csv', chemicaltable = 'ChemicalTable.csv'):
        self.ions = {} #Key: Chem Symbol, Value: name, weight
        self.ionkeys = [] #List of available ions by formula
        self.chemicalkeys = []#List of available chemicals by formula
        self.chemicals = {}#Imported CSV of chemicals Value: NamedTuple
        self.targetions = {}
        self.targetionkeys = []

        with open(iontable) as f:
            table = csv.reader(f)
            header = next(table)
            SaltIon = namedtuple("SaltIon", header)
            SaltIonTarget = namedtuple("SaltIonTarget", header)
            for row in table:
                if row == header:
                    break
                symbol = row[1]
                self.ions[symbol] = SaltIon(*row)
            for row in table:
                symbol = row[1]
                self.targetions[symbol] = SaltIonTarget(*row)
            self.ionkeys = list(self.ions.keys())
            self.targetionkeys = list(self.targetions.keys())
            print(self.ionkeys,self.targetionkeys)

        with open(chemicaltable) as f:
            table = csv.reader(f)
            skip = next(table)#Skip First Row
            header = next(table) #Headers are second row
            Chemical = namedtuple("Chemical", header)
            for row in table:
                formula = row[0]
                self.chemicals[formula] = Chemical(*row)
            self.chemicalkeys = list(self.chemicals.keys())