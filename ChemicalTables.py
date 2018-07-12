import csv
from collections import namedtuple


class Ions:
    def __init__(self, iontable = 'IonTable.csv', chemicaltable = 'ChemicalTable.csv'):
        self.ions = {} #Key: Chem Symbol, Value: name, weight
        self.ionkeys = [] #List of available ions by formula
        self.chemicalkeys = []#List of available chemicals by formula
        self.chemicals = {}#Imported CSV of chemicals Value: NamedTuple

        with open(iontable) as f:
            table = csv.reader(f)
            tablelist = list(table)
            for i in range(1, len(tablelist[0])):
                symbol = tablelist[1][i]
                name = tablelist[0][i]
                weight = tablelist[2][i]
                items = [name, weight]
                self.ions[symbol] = items
            self.ionkeys = list(self.ions.keys())

        with open(chemicaltable) as f:
            table = csv.reader(f)
            skip = next(table)#Skip First Row
            header = next(table) #Headers are second row
            Chemical = namedtuple("Chemical", header)
            for row in table:
                formula = row[0]
                self.chemicals[formula] = Chemical(*row)
            self.chemicalkeys = list(self.chemicals.keys())