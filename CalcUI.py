# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalcUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1057, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuStarting_Salt = QtWidgets.QMenu(self.menuFile)
        self.menuStarting_Salt.setObjectName("menuStarting_Salt")
        self.menuDesired_Salt = QtWidgets.QMenu(self.menuFile)
        self.menuDesired_Salt.setObjectName("menuDesired_Salt")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCalculate = QtWidgets.QAction(MainWindow)
        self.actionCalculate.setCheckable(False)
        self.actionCalculate.setObjectName("actionCalculate")
        self.actionLoad_Starting_PPM = QtWidgets.QAction(MainWindow)
        self.actionLoad_Starting_PPM.setObjectName("actionLoad_Starting_PPM")
        self.actionSave_Starting_PPM = QtWidgets.QAction(MainWindow)
        self.actionSave_Starting_PPM.setObjectName("actionSave_Starting_PPM")
        self.actionLoad_desired_PPM = QtWidgets.QAction(MainWindow)
        self.actionLoad_desired_PPM.setObjectName("actionLoad_desired_PPM")
        self.actionSave_desired_PPM = QtWidgets.QAction(MainWindow)
        self.actionSave_desired_PPM.setObjectName("actionSave_desired_PPM")
        self.menuStarting_Salt.addAction(self.actionLoad_Starting_PPM)
        self.menuStarting_Salt.addAction(self.actionSave_Starting_PPM)
        self.menuDesired_Salt.addAction(self.actionLoad_desired_PPM)
        self.menuDesired_Salt.addAction(self.actionSave_desired_PPM)
        self.menuFile.addAction(self.actionCalculate)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuStarting_Salt.menuAction())
        self.menuFile.addAction(self.menuDesired_Salt.menuAction())
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
        self.menuStarting_Salt.setTitle(_translate("MainWindow", "Starting Salt"))
        self.menuDesired_Salt.setTitle(_translate("MainWindow", "Desired Salt"))
        self.actionCalculate.setText(_translate("MainWindow", "Calculate"))
        self.actionLoad_Starting_PPM.setText(_translate("MainWindow", "Load starting PPM"))
        self.actionSave_Starting_PPM.setText(_translate("MainWindow", "Save starting PPM"))
        self.actionLoad_desired_PPM.setText(_translate("MainWindow", "Load desired PPM"))
        self.actionSave_desired_PPM.setText(_translate("MainWindow", "Save desired PPM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

