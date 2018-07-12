# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalcUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ChemicalTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ChemicalTable.setObjectName("ChemicalTable")
        self.ChemicalTable.setColumnCount(0)
        self.ChemicalTable.setRowCount(0)
        self.horizontalLayout.addWidget(self.ChemicalTable)
        self.saltDesiredBox = QtWidgets.QGroupBox(self.centralwidget)
        self.saltDesiredBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.saltDesiredBox.setObjectName("saltDesiredBox")
        self.horizontalLayout.addWidget(self.saltDesiredBox)
        self.saltRequiredBox = QtWidgets.QGroupBox(self.centralwidget)
        self.saltRequiredBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.saltRequiredBox.setObjectName("saltRequiredBox")
        self.horizontalLayout.addWidget(self.saltRequiredBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCalculate = QtWidgets.QAction(MainWindow)
        self.actionCalculate.setCheckable(False)
        self.actionCalculate.setObjectName("actionCalculate")
        self.actionLoad_Current_Slats = QtWidgets.QAction(MainWindow)
        self.actionLoad_Current_Slats.setObjectName("actionLoad_Current_Slats")
        self.menuFile.addAction(self.actionCalculate)
        self.menuFile.addAction(self.actionLoad_Current_Slats)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saltDesiredBox.setTitle(_translate("MainWindow", "Desired ppm levels"))
        self.saltRequiredBox.setTitle(_translate("MainWindow", "Required Salt Amounts"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionCalculate.setText(_translate("MainWindow", "Calculate"))
        self.actionLoad_Current_Slats.setText(_translate("MainWindow", "Load Current Salts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

