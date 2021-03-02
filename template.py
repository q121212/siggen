# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_signalGeneratorMainWindow(object):
    def setupUi(self, signalGeneratorMainWindow):
        signalGeneratorMainWindow.setObjectName("signalGeneratorMainWindow")
        signalGeneratorMainWindow.resize(685, 567)
        self.centralwidget = QtWidgets.QWidget(signalGeneratorMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 0, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 31, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 110, 101, 21))
        self.label_4.setObjectName("label_4")
        self.urlLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.urlLineEdit.setGeometry(QtCore.QRect(30, 30, 621, 21))
        self.urlLineEdit.setObjectName("urlLineEdit")
        self.btnCalculateSignal = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.btnCalculateSignal.setGeometry(QtCore.QRect(540, 90, 141, 31))
        self.btnCalculateSignal.setObjectName("btnCalculateSignal")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 130, 681, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.signalTypeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.signalTypeComboBox.setGeometry(QtCore.QRect(110, 70, 161, 21))
        self.signalTypeComboBox.setObjectName("signalTypeComboBox")
        self.exportFormatComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.exportFormatComboBox.setGeometry(QtCore.QRect(110, 110, 81, 21))
        self.exportFormatComboBox.setObjectName("exportFormatComboBox")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(-15, 141, 701, 381))
        self.graphicsView.setObjectName("graphicsView")
        signalGeneratorMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(signalGeneratorMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        signalGeneratorMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(signalGeneratorMainWindow)
        self.statusbar.setObjectName("statusbar")
        signalGeneratorMainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(signalGeneratorMainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(signalGeneratorMainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(signalGeneratorMainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_All = QtGui.QAction(signalGeneratorMainWindow)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionAbout = QtGui.QAction(signalGeneratorMainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtGui.QAction(signalGeneratorMainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPreferences = QtGui.QAction(signalGeneratorMainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_All)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(signalGeneratorMainWindow)
        QtCore.QMetaObject.connectSlotsByName(signalGeneratorMainWindow)

    def retranslateUi(self, signalGeneratorMainWindow):
        _translate = QtCore.QCoreApplication.translate
        signalGeneratorMainWindow.setWindowTitle(_translate("signalGeneratorMainWindow", "Signal generator"))
        self.label.setText(_translate("signalGeneratorMainWindow", "Parameters"))
        self.label_2.setText(_translate("signalGeneratorMainWindow", "Url:"))
        self.label_3.setText(_translate("signalGeneratorMainWindow", "Signal type:"))
        self.label_4.setText(_translate("signalGeneratorMainWindow", "Export format:"))
        self.urlLineEdit.setText(_translate("signalGeneratorMainWindow", "http://"))
        self.btnCalculateSignal.setText(_translate("signalGeneratorMainWindow", "Calculate signal"))
        self.menuFile.setTitle(_translate("signalGeneratorMainWindow", "File"))
        self.menuSettings.setTitle(_translate("signalGeneratorMainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("signalGeneratorMainWindow", "Help"))
        self.actionNew.setText(_translate("signalGeneratorMainWindow", "New"))
        self.actionOpen.setText(_translate("signalGeneratorMainWindow", "Open"))
        self.actionSave.setText(_translate("signalGeneratorMainWindow", "Save"))
        self.actionSave_All.setText(_translate("signalGeneratorMainWindow", "Save All"))
        self.actionAbout.setText(_translate("signalGeneratorMainWindow", "About"))
        self.actionQuit.setText(_translate("signalGeneratorMainWindow", "Quit"))
        self.actionPreferences.setText(_translate("signalGeneratorMainWindow", "Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signalGeneratorMainWindow = QtWidgets.QMainWindow()
    ui = Ui_signalGeneratorMainWindow()
    ui.setupUi(signalGeneratorMainWindow)
    signalGeneratorMainWindow.show()
    sys.exit(app.exec())
