from CalcUI import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ChemicalTables import Ions
from chemspipy import ChemSpider


cs = ChemSpider('59fce5c4-bef3-4e84-9a72-2a0ef4bc6538')

class CalculatorMain(Ui_MainWindow):
    def __init__(self, mWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mWindow)

        self.Ions = Ions()

        self.setupTable()

    def setupTable(self):
        ncolumns = 4
        nrows = len(self.Ions.chemicalkeys)

        self.ChemicalTable.setRowCount(nrows)
        self.ChemicalTable.setColumnCount(ncolumns)

        headerkeys = ['Formula','Name','constituent1','constituent2']
        i, j = 0, 0
        for chemical in self.Ions.chemicalkeys:
            j = 0
            for header in headerkeys:
                item = getattr(self.Ions.chemicals[chemical], header)
                qitem = QtWidgets.QTableWidgetItem(item)
                self.ChemicalTable.setItem(i,j,qitem)
                j += 1
            i +=1

        Headeritems = ['Formula','Name','Ion #1','Ion #2']
        i = 0
        for item in Headeritems:
            header = QtWidgets.QTableWidgetItem(item)
            self.ChemicalTable.setHorizontalHeaderItem(i, header)
            i += 1









if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mWindow = QtWidgets.QMainWindow()

    prog = CalculatorMain(mWindow)
    mWindow.show()
    sys.exit(app.exec_())