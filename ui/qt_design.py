# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(460, 401)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_ports = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_ports.setObjectName("comboBox_ports")
        self.horizontalLayout_2.addWidget(self.comboBox_ports)
        self.pushButton_refresh = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_refresh.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout_2.addWidget(self.pushButton_refresh)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_baudrate = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_baudrate.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_baudrate.setObjectName("label_baudrate")
        self.horizontalLayout.addWidget(self.label_baudrate)
        self.comboBox_baudrate = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_baudrate.setCurrentText("9600")
        self.comboBox_baudrate.setObjectName("comboBox_baudrate")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.comboBox_baudrate.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_baudrate)
        self.pushButton_connect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_connect.sizePolicy().hasHeightForWidth())
        self.pushButton_connect.setSizePolicy(sizePolicy)
        self.pushButton_connect.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.horizontalLayout.addWidget(self.pushButton_connect)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.textEdit_terminal = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_terminal.setReadOnly(True)
        self.textEdit_terminal.setObjectName("textEdit_terminal")
        self.verticalLayout_3.addWidget(self.textEdit_terminal)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_send = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_send.setObjectName("lineEdit_send")
        self.horizontalLayout_3.addWidget(self.lineEdit_send)
        self.pushButton_send = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_send.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout_3.addWidget(self.pushButton_send)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox_baudrate.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial Disposer"))
        self.pushButton_refresh.setText(_translate("MainWindow", "Refresh"))
        self.label_baudrate.setText(_translate("MainWindow", "Select baudrate:"))
        self.comboBox_baudrate.setItemText(0, _translate("MainWindow", "300"))
        self.comboBox_baudrate.setItemText(1, _translate("MainWindow", "1200"))
        self.comboBox_baudrate.setItemText(2, _translate("MainWindow", "2400"))
        self.comboBox_baudrate.setItemText(3, _translate("MainWindow", "4800"))
        self.comboBox_baudrate.setItemText(4, _translate("MainWindow", "9600"))
        self.comboBox_baudrate.setItemText(5, _translate("MainWindow", "19200"))
        self.comboBox_baudrate.setItemText(6, _translate("MainWindow", "38400"))
        self.comboBox_baudrate.setItemText(7, _translate("MainWindow", "57600"))
        self.comboBox_baudrate.setItemText(8, _translate("MainWindow", "74880"))
        self.comboBox_baudrate.setItemText(9, _translate("MainWindow", "115200"))
        self.comboBox_baudrate.setItemText(10, _translate("MainWindow", "230400"))
        self.comboBox_baudrate.setItemText(11, _translate("MainWindow", "250000"))
        self.comboBox_baudrate.setItemText(12, _translate("MainWindow", "500000"))
        self.comboBox_baudrate.setItemText(13, _translate("MainWindow", "1000000"))
        self.comboBox_baudrate.setItemText(14, _translate("MainWindow", "2000000"))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect"))
        self.pushButton_send.setText(_translate("MainWindow", "Send"))
