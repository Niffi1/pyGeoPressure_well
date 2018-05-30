# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smooth_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_smooth_Dialog(object):
    def setupUi(self, smooth_Dialog):
        smooth_Dialog.setObjectName(_fromUtf8("smooth_Dialog"))
        smooth_Dialog.resize(550, 755)
        self.horizontalLayout = QtGui.QHBoxLayout(smooth_Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(smooth_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 20, 31, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.well_comboBox = QtGui.QComboBox(self.groupBox)
        self.well_comboBox.setGeometry(QtCore.QRect(40, 20, 81, 20))
        self.well_comboBox.setObjectName(_fromUtf8("well_comboBox"))
        self.log_comboBox = QtGui.QComboBox(self.groupBox)
        self.log_comboBox.setGeometry(QtCore.QRect(10, 70, 111, 20))
        self.log_comboBox.setObjectName(_fromUtf8("log_comboBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 31, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 300, 141, 231))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.plot_horizon_Button = QtGui.QPushButton(self.groupBox_2)
        self.plot_horizon_Button.setGeometry(QtCore.QRect(60, 200, 65, 23))
        self.plot_horizon_Button.setObjectName(_fromUtf8("plot_horizon_Button"))
        self.horizon_listWidget = QtGui.QListWidget(self.groupBox_2)
        self.horizon_listWidget.setGeometry(QtCore.QRect(10, 20, 121, 171))
        self.horizon_listWidget.setProperty("isWrapping", True)
        self.horizon_listWidget.setObjectName(_fromUtf8("horizon_listWidget"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 230, 111, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.save_Button = QtGui.QPushButton(self.groupBox)
        self.save_Button.setGeometry(QtCore.QRect(60, 260, 65, 23))
        self.save_Button.setObjectName(_fromUtf8("save_Button"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 100, 141, 121))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.smooth_Button = QtGui.QPushButton(self.groupBox_3)
        self.smooth_Button.setGeometry(QtCore.QRect(60, 80, 65, 23))
        self.smooth_Button.setObjectName(_fromUtf8("smooth_Button"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 41, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.times_spinBox = QtGui.QSpinBox(self.groupBox_3)
        self.times_spinBox.setGeometry(QtCore.QRect(50, 20, 71, 22))
        self.times_spinBox.setSuffix(_fromUtf8(""))
        self.times_spinBox.setMinimum(1)
        self.times_spinBox.setMaximum(30)
        self.times_spinBox.setProperty("value", 1)
        self.times_spinBox.setObjectName(_fromUtf8("times_spinBox"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(0, 50, 41, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.window_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.window_lineEdit.setGeometry(QtCore.QRect(50, 50, 71, 20))
        self.window_lineEdit.setObjectName(_fromUtf8("window_lineEdit"))
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(smooth_Dialog)
        QtCore.QMetaObject.connectSlotsByName(smooth_Dialog)

    def retranslateUi(self, smooth_Dialog):
        smooth_Dialog.setWindowTitle(_translate("smooth_Dialog", "Smooth Log", None))
        self.groupBox.setTitle(_translate("smooth_Dialog", "Data", None))
        self.label.setText(_translate("smooth_Dialog", "Well", None))
        self.label_2.setText(_translate("smooth_Dialog", "Log", None))
        self.groupBox_2.setTitle(_translate("smooth_Dialog", "Horizons", None))
        self.plot_horizon_Button.setText(_translate("smooth_Dialog", "Plot", None))
        self.lineEdit.setText(_translate("smooth_Dialog", "_sm{times}", None))
        self.save_Button.setText(_translate("smooth_Dialog", "Save", None))
        self.groupBox_3.setTitle(_translate("smooth_Dialog", "Smooth", None))
        self.smooth_Button.setText(_translate("smooth_Dialog", "Smooth", None))
        self.label_3.setText(_translate("smooth_Dialog", "Times", None))
        self.label_4.setText(_translate("smooth_Dialog", "Window", None))
        self.window_lineEdit.setText(_translate("smooth_Dialog", "1500", None))

