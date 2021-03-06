# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1680, 691)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 1661, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_calib = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_calib.setObjectName("btn_calib")
        self.horizontalLayout.addWidget(self.btn_calib)
        self.btn_calib_save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_calib_save.setObjectName("btn_calib_save")
        self.horizontalLayout.addWidget(self.btn_calib_save)
        self.btn_start_loop = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_start_loop.setObjectName("btn_start_loop")
        self.horizontalLayout.addWidget(self.btn_start_loop)
        self.btn_stop_loop = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_stop_loop.setObjectName("btn_stop_loop")
        self.horizontalLayout.addWidget(self.btn_stop_loop)
        self.btn_exit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        self.labelAutoManual = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAutoManual.sizePolicy().hasHeightForWidth())
        self.labelAutoManual.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelAutoManual.setFont(font)
        self.labelAutoManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAutoManual.setObjectName("labelAutoManual")
        self.horizontalLayout.addWidget(self.labelAutoManual)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 150, 1661, 311))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.labelBlue = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBlue.sizePolicy().hasHeightForWidth())
        self.labelBlue.setSizePolicy(sizePolicy)
        self.labelBlue.setMaximumSize(QtCore.QSize(16777215, 255))
        self.labelBlue.setText("")
        self.labelBlue.setScaledContents(True)
        self.labelBlue.setObjectName("labelBlue")
        self.verticalLayout_2.addWidget(self.labelBlue)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.labelGreen = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelGreen.sizePolicy().hasHeightForWidth())
        self.labelGreen.setSizePolicy(sizePolicy)
        self.labelGreen.setMaximumSize(QtCore.QSize(16777215, 255))
        self.labelGreen.setText("")
        self.labelGreen.setScaledContents(True)
        self.labelGreen.setObjectName("labelGreen")
        self.verticalLayout_3.addWidget(self.labelGreen)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.labelRed = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRed.sizePolicy().hasHeightForWidth())
        self.labelRed.setSizePolicy(sizePolicy)
        self.labelRed.setMaximumSize(QtCore.QSize(16777215, 255))
        self.labelRed.setText("")
        self.labelRed.setScaledContents(True)
        self.labelRed.setObjectName("labelRed")
        self.verticalLayout.addWidget(self.labelRed)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.labelNIR = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNIR.sizePolicy().hasHeightForWidth())
        self.labelNIR.setSizePolicy(sizePolicy)
        self.labelNIR.setMaximumSize(QtCore.QSize(16777215, 255))
        self.labelNIR.setText("")
        self.labelNIR.setScaledContents(True)
        self.labelNIR.setObjectName("labelNIR")
        self.verticalLayout_4.addWidget(self.labelNIR)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.logoSE = QtWidgets.QLabel(self.centralwidget)
        self.logoSE.setGeometry(QtCore.QRect(10, 10, 271, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoSE.sizePolicy().hasHeightForWidth())
        self.logoSE.setSizePolicy(sizePolicy)
        self.logoSE.setText("")
        self.logoSE.setPixmap(QtGui.QPixmap(":/logoSE/LOGO-SE-2018.png"))
        self.logoSE.setScaledContents(True)
        self.logoSE.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.logoSE.setObjectName("logoSE")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 470, 1661, 111))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.comboBoxMode = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBoxMode.setObjectName("comboBoxMode")
        self.comboBoxMode.addItem("")
        self.comboBoxMode.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBoxMode)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.checkBoxDarkFilter = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxDarkFilter.sizePolicy().hasHeightForWidth())
        self.checkBoxDarkFilter.setSizePolicy(sizePolicy)
        self.checkBoxDarkFilter.setText("")
        self.checkBoxDarkFilter.setObjectName("checkBoxDarkFilter")
        self.horizontalLayout_12.addWidget(self.checkBoxDarkFilter)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_15.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        self.spinBoxShutter = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBoxShutter.setMaximum(7718085)
        self.spinBoxShutter.setObjectName("spinBoxShutter")
        self.horizontalLayout_3.addWidget(self.spinBoxShutter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.checkBoxVignetting = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxVignetting.sizePolicy().hasHeightForWidth())
        self.checkBoxVignetting.setSizePolicy(sizePolicy)
        self.checkBoxVignetting.setText("")
        self.checkBoxVignetting.setObjectName("checkBoxVignetting")
        self.horizontalLayout_4.addWidget(self.checkBoxVignetting)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_15.addLayout(self.verticalLayout_5)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_6.addWidget(self.label_24)
        self.spinBoxGain = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBoxGain.setMaximum(254)
        self.spinBoxGain.setObjectName("spinBoxGain")
        self.horizontalLayout_6.addWidget(self.spinBoxGain)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_14.addWidget(self.label_14)
        self.checkBoxCalibration = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxCalibration.sizePolicy().hasHeightForWidth())
        self.checkBoxCalibration.setSizePolicy(sizePolicy)
        self.checkBoxCalibration.setText("")
        self.checkBoxCalibration.setObjectName("checkBoxCalibration")
        self.horizontalLayout_14.addWidget(self.checkBoxCalibration)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_14)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_15.addLayout(self.verticalLayout_10)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_10.addWidget(self.label_28)
        self.spinBoxX1 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBoxX1.setMaximum(1279)
        self.spinBoxX1.setObjectName("spinBoxX1")
        self.horizontalLayout_10.addWidget(self.spinBoxX1)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_29 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_11.addWidget(self.label_29)
        self.spinBoxY1 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBoxY1.setMaximum(799)
        self.spinBoxY1.setObjectName("spinBoxY1")
        self.horizontalLayout_11.addWidget(self.spinBoxY1)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.horizontalLayout_15.addLayout(self.verticalLayout_13)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_8.addWidget(self.label_26)
        self.spinBoxX2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBoxX2.setMaximum(1279)
        self.spinBoxX2.setObjectName("spinBoxX2")
        self.horizontalLayout_8.addWidget(self.spinBoxX2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_27 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_9.addWidget(self.label_27)
        self.spinBoxY2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBoxY2.setMaximum(799)
        self.spinBoxY2.setObjectName("spinBoxY2")
        self.horizontalLayout_9.addWidget(self.spinBoxY2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.verticalLayout_7.addLayout(self.verticalLayout_11)
        self.horizontalLayout_15.addLayout(self.verticalLayout_7)
        self.buttonSaveParameters = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.buttonSaveParameters.setObjectName("buttonSaveParameters")
        self.horizontalLayout_15.addWidget(self.buttonSaveParameters)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1100, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 610, 1661, 45))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.labelMsg = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMsg.sizePolicy().hasHeightForWidth())
        self.labelMsg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelMsg.setFont(font)
        self.labelMsg.setObjectName("labelMsg")
        self.horizontalLayout_13.addWidget(self.labelMsg)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "M7L"))
        self.btn_calib.setText(_translate("MainWindow", "Calibration"))
        self.btn_calib_save.setText(_translate("MainWindow", "Save"))
        self.btn_start_loop.setText(_translate("MainWindow", "Start"))
        self.btn_stop_loop.setText(_translate("MainWindow", "Stop"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.labelAutoManual.setText(_translate("MainWindow", "Manual"))
        self.label_2.setText(_translate("MainWindow", "Blue"))
        self.label_4.setText(_translate("MainWindow", "Green"))
        self.label_6.setText(_translate("MainWindow", "Red"))
        self.label_8.setText(_translate("MainWindow", "NIR"))
        self.label.setText(_translate("MainWindow", "Mode"))
        self.comboBoxMode.setItemText(0, _translate("MainWindow", "Manual"))
        self.comboBoxMode.setItemText(1, _translate("MainWindow", "Automatic"))
        self.label_3.setText(_translate("MainWindow", "Dark Filter"))
        self.label_12.setText(_translate("MainWindow", "Shutter (us)"))
        self.label_13.setText(_translate("MainWindow", "Vignetting"))
        self.label_24.setText(_translate("MainWindow", "Gain"))
        self.label_14.setText(_translate("MainWindow", "Radiometric Calibration"))
        self.label_28.setText(_translate("MainWindow", "X1"))
        self.label_29.setText(_translate("MainWindow", "Y1"))
        self.label_26.setText(_translate("MainWindow", "X2"))
        self.label_27.setText(_translate("MainWindow", "Y2"))
        self.buttonSaveParameters.setText(_translate("MainWindow", "Save Config"))
        self.label_5.setText(_translate("MainWindow", "M7L"))
        self.labelMsg.setText(_translate("MainWindow", "Message"))
import gui_rc
