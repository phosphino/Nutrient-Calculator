from CalcUI import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ChemicalTables import Ions
from chemspipy import ChemSpider

cs = ChemSpider('59fce5c4-bef3-4e84-9a72-2a0ef4bc6538')


class CalculatorMain(Ui_MainWindow):
	def __init__(self, mWindow):
		Ui_MainWindow.__init__(self)
		self.mWindow = mWindow
		self.setupUi(mWindow)
		self.actionSave_Starting_PPM.triggered.connect(self.savestartingsalt)

		self.Ions = Ions()

		self.chemicalavailability = {}  # Keys: Chemical Formula, Values: CheckBox for availability
		self.startingPPM = {}
		self.desiredPPM = {}

		self.setupTable()
		self.setupStartingBox()
		self.setDesiredBox()


	def savestartingsalt(self):
		file = QtWidgets.QFileDialog.getSaveFileName(self.mWindow,
													 'Save Starting Salt PPM',
													 'C:\\Users\\Andy\\Documents\\GitHub\\Nutrient-Calculator',
													 "CSV (*.csv)")
		header = ['symbol', 'ppm']
		

	def setDesiredBox(self):
		mainvbox = QtWidgets.QVBoxLayout()
		for ions in sorted(self.Ions.targetions):
			hbox = QtWidgets.QHBoxLayout()

			ions = ions.rstrip()
			qlabel = QtWidgets.QLabel(ions)
			qlabel.setMaximumWidth(30)
			qppmdesirededit = QtWidgets.QLineEdit()
			qppmdesirededit.setMaximumWidth(40)
			qlabelunits = QtWidgets.QLabel('ppm')
			self.desiredPPM[ions] = qppmdesirededit


			hbox.addWidget(qlabel)
			hbox.addWidget(qppmdesirededit)
			hbox.addWidget(qlabelunits)

			mainvbox.addLayout(hbox)

		self.saltDesiredBox.setLayout(mainvbox)

	def setupRequiredBox(self):
		mainvbox = QtWidgets.QVBoxLayout()

	def setupStartingBox(self):
		mainvbox = QtWidgets.QVBoxLayout()

		for ions in sorted(self.Ions.ions):
			hbox = QtWidgets.QHBoxLayout()

			qlabel = QtWidgets.QLabel(str(ions).rstrip())
			qlabel.setMaximumWidth(30)
			qppmstartedit = QtWidgets.QLineEdit()
			qppmstartedit.setMaximumWidth(40)
			qlabelunits = QtWidgets.QLabel('ppm')

			hbox.addWidget(qlabel)
			hbox.addWidget(qppmstartedit)
			hbox.addWidget(qlabelunits)
			mainvbox.addLayout(hbox)
			self.startingPPM[str(ions)] = qppmstartedit

		self.saltStartingBox.setLayout(mainvbox)

	def setupTable(self):  # Sets up the table containing the available salts
		ncolumns = 4
		nrows = len(self.Ions.chemicalkeys)

		self.ChemicalTable.setRowCount(nrows)
		self.ChemicalTable.setColumnCount(ncolumns)

		headerkeys = ['Formula', 'Name', 'constituent1', 'constituent2']
		i, j = 0, 0
		for chemical in self.Ions.chemicalkeys:
			j = 0
			for header in headerkeys:
				item = getattr(self.Ions.chemicals[chemical], header)
				qitem = QtWidgets.QTableWidgetItem(item)
				if j == 0:
					btn = QtWidgets.QCheckBox(self.ChemicalTable)
					btn.setText(item)
					self.ChemicalTable.setCellWidget(i, j, btn)
					self.chemicalavailability[item] = btn
				else:
					self.ChemicalTable.setItem(i, j, qitem)
				j += 1
			i += 1

		Headeritems = ['Formula', 'Name', 'Ion #1', 'Ion #2']
		i = 0
		for item in Headeritems:
			header = QtWidgets.QTableWidgetItem(item)
			self.ChemicalTable.setHorizontalHeaderItem(i, header)
			i += 1

		self.ChemicalTable.resizeColumnsToContents()
		columnwidth = 0
		for i in range(4):
			columnwidth += self.ChemicalTable.columnWidth(i)
		columnwidth += self.ChemicalTable.verticalHeader().width()
		self.ChemicalTable.setMaximumWidth(columnwidth + 24)


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	mWindow = QtWidgets.QMainWindow()

	prog = CalculatorMain(mWindow)
	mWindow.show()
	sys.exit(app.exec_())
