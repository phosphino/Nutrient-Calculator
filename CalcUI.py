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
        MainWindow.resize(1057, 704)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ChemicalTable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChemicalTable.sizePolicy().hasHeightForWidth())
        self.ChemicalTable.setSizePolicy(sizePolicy)
        self.ChemicalTable.setMaximumSize(QtCore.QSize(200000, 16777215))
        self.ChemicalTable.setObjectName("ChemicalTable")
        self.ChemicalTable.setColumnCount(0)
        self.ChemicalTable.setRowCount(0)
        self.horizontalLayout.addWidget(self.ChemicalTable)
        self.saltStartingBox = QtWidgets.QGroupBox(self.centralwidget)
        self.saltStartingBox.setMaximumSize(QtCore.QSize(625, 16777215))
        self.saltStartingBox.setObjectName("saltStartingBox")
        self.horizontalLayout.addWidget(self.saltStartingBox)
        self.saltDesiredBox = QtWidgets.QGroupBox(self.centralwidget)
        self.saltDesiredBox.setMaximumSize(QtCore.QSize(625, 16777215))
        self.saltDesiredBox.setObjectName("saltDesiredBox")
        self.horizontalLayout.addWidget(self.saltDesiredBox)
        self.RequiredList = QtWidgets.QListView(self.centralwidget)
        self.RequiredList.setMaximumSize(QtCore.QSize(400, 16777215))
        self.RequiredList.setObjectName("RequiredList")
        self.horizontalLayout.addWidget(self.RequiredList)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1057, 26))
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
        self.ChemicalTable.setSortingEnabled(True)
        self.saltStartingBox.setTitle(_translate("MainWindow", "Starting Salt ppm Levels"))
        self.saltDesiredBox.setTitle(_translate("MainWindow", "Desired ppm Levels"))
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

