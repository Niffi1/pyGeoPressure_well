# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optimize_bowers_dialog.ui'
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

class Ui_optimize_bowers_Dialog(object):
    def setupUi(self, optimize_bowers_Dialog):
        optimize_bowers_Dialog.setObjectName(_fromUtf8("optimize_bowers_Dialog"))
        optimize_bowers_Dialog.resize(867, 545)
        self.horizontalLayout = QtGui.QHBoxLayout(optimize_bowers_Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(optimize_bowers_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.well_listWidget = QtGui.QListWidget(self.groupBox)
        self.well_listWidget.setGeometry(QtCore.QRect(0, 20, 131, 151))
        self.well_listWidget.setObjectName(_fromUtf8("well_listWidget"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 51, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.velocity_comboBox = QtGui.QComboBox(self.groupBox)
        self.velocity_comboBox.setGeometry(QtCore.QRect(10, 190, 121, 22))
        self.velocity_comboBox.setObjectName(_fromUtf8("velocity_comboBox"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 51, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 51, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.obp_comboBox = QtGui.QComboBox(self.groupBox)
        self.obp_comboBox.setGeometry(QtCore.QRect(10, 230, 121, 22))
        self.obp_comboBox.setObjectName(_fromUtf8("obp_comboBox"))
        self.scatter_Button = QtGui.QPushButton(self.groupBox)
        self.scatter_Button.setGeometry(QtCore.QRect(60, 380, 65, 23))
        self.scatter_Button.setObjectName(_fromUtf8("scatter_Button"))
        self.pres_listWidget = QtGui.QListWidget(self.groupBox)
        self.pres_listWidget.setGeometry(QtCore.QRect(0, 270, 131, 101))
        self.pres_listWidget.setObjectName(_fromUtf8("pres_listWidget"))
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_4 = QtGui.QGroupBox(optimize_bowers_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 360, 141, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.save_Button = QtGui.QPushButton(self.groupBox_2)
        self.save_Button.setGeometry(QtCore.QRect(60, 50, 65, 23))
        self.save_Button.setObjectName(_fromUtf8("save_Button"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 20, 141, 171))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.fit_loading_Button = QtGui.QPushButton(self.groupBox_3)
        self.fit_loading_Button.setGeometry(QtCore.QRect(0, 120, 60, 23))
        self.fit_loading_Button.setObjectName(_fromUtf8("fit_loading_Button"))
        self.a_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.a_lineEdit.setGeometry(QtCore.QRect(40, 20, 91, 20))
        self.a_lineEdit.setObjectName(_fromUtf8("a_lineEdit"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(11, 20, 20, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(11, 40, 20, 20))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.b_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.b_lineEdit.setGeometry(QtCore.QRect(40, 40, 91, 20))
        self.b_lineEdit.setObjectName(_fromUtf8("b_lineEdit"))
        self.draw_loading_Button = QtGui.QPushButton(self.groupBox_3)
        self.draw_loading_Button.setGeometry(QtCore.QRect(70, 120, 60, 23))
        self.draw_loading_Button.setObjectName(_fromUtf8("draw_loading_Button"))
        self.clear_loading_Button = QtGui.QPushButton(self.groupBox_3)
        self.clear_loading_Button.setGeometry(QtCore.QRect(70, 140, 60, 23))
        self.clear_loading_Button.setObjectName(_fromUtf8("clear_loading_Button"))
        self.loading_textEdit = QtGui.QTextEdit(self.groupBox_3)
        self.loading_textEdit.setGeometry(QtCore.QRect(0, 60, 131, 51))
        self.loading_textEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.loading_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.loading_textEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.loading_textEdit.setReadOnly(True)
        self.loading_textEdit.setObjectName(_fromUtf8("loading_textEdit"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 190, 141, 171))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.fit_unloading_Button = QtGui.QPushButton(self.groupBox_5)
        self.fit_unloading_Button.setGeometry(QtCore.QRect(0, 120, 60, 23))
        self.fit_unloading_Button.setObjectName(_fromUtf8("fit_unloading_Button"))
        self.label_14 = QtGui.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 31, 20))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.vmax_lineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.vmax_lineEdit.setGeometry(QtCore.QRect(50, 40, 61, 20))
        self.vmax_lineEdit.setObjectName(_fromUtf8("vmax_lineEdit"))
        self.u_lineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.u_lineEdit.setGeometry(QtCore.QRect(50, 20, 81, 20))
        self.u_lineEdit.setObjectName(_fromUtf8("u_lineEdit"))
        self.label_15 = QtGui.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 31, 20))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.draw_unloading_Button = QtGui.QPushButton(self.groupBox_5)
        self.draw_unloading_Button.setGeometry(QtCore.QRect(70, 120, 60, 23))
        self.draw_unloading_Button.setObjectName(_fromUtf8("draw_unloading_Button"))
        self.clear_unloading_Button = QtGui.QPushButton(self.groupBox_5)
        self.clear_unloading_Button.setGeometry(QtCore.QRect(70, 140, 60, 23))
        self.clear_unloading_Button.setObjectName(_fromUtf8("clear_unloading_Button"))
        self.unloading_textEdit = QtGui.QTextEdit(self.groupBox_5)
        self.unloading_textEdit.setGeometry(QtCore.QRect(0, 60, 131, 51))
        self.unloading_textEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.unloading_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.unloading_textEdit.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.unloading_textEdit.setReadOnly(True)
        self.unloading_textEdit.setObjectName(_fromUtf8("unloading_textEdit"))
        self.horizontalLayout.addWidget(self.groupBox_4)

        self.retranslateUi(optimize_bowers_Dialog)
        QtCore.QMetaObject.connectSlotsByName(optimize_bowers_Dialog)

    def retranslateUi(self, optimize_bowers_Dialog):
        optimize_bowers_Dialog.setWindowTitle(_translate("optimize_bowers_Dialog", "Optimize Bowers", None))
        self.groupBox.setTitle(_translate("optimize_bowers_Dialog", "Wells", None))
        self.label_5.setText(_translate("optimize_bowers_Dialog", "Velocity:", None))
        self.label_7.setText(_translate("optimize_bowers_Dialog", "Pressure:", None))
        self.label_6.setText(_translate("optimize_bowers_Dialog", "OBP:", None))
        self.scatter_Button.setText(_translate("optimize_bowers_Dialog", "Scatter", None))
        self.groupBox_4.setTitle(_translate("optimize_bowers_Dialog", "Optimize", None))
        self.groupBox_2.setTitle(_translate("optimize_bowers_Dialog", "Save", None))
        self.save_Button.setText(_translate("optimize_bowers_Dialog", "Save", None))
        self.lineEdit.setText(_translate("optimize_bowers_Dialog", "N", None))
        self.groupBox_3.setTitle(_translate("optimize_bowers_Dialog", "Loading", None))
        self.fit_loading_Button.setText(_translate("optimize_bowers_Dialog", "Fit", None))
        self.a_lineEdit.setText(_translate("optimize_bowers_Dialog", "98", None))
        self.label_12.setText(_translate("optimize_bowers_Dialog", "A:", None))
        self.label_13.setText(_translate("optimize_bowers_Dialog", "B:", None))
        self.b_lineEdit.setText(_translate("optimize_bowers_Dialog", "0.86", None))
        self.draw_loading_Button.setText(_translate("optimize_bowers_Dialog", "Draw", None))
        self.clear_loading_Button.setText(_translate("optimize_bowers_Dialog", "Clear", None))
        self.groupBox_5.setTitle(_translate("optimize_bowers_Dialog", "Unloading", None))
        self.fit_unloading_Button.setText(_translate("optimize_bowers_Dialog", "Fit", None))
        self.label_14.setText(_translate("optimize_bowers_Dialog", "U:", None))
        self.vmax_lineEdit.setText(_translate("optimize_bowers_Dialog", "4800", None))
        self.u_lineEdit.setText(_translate("optimize_bowers_Dialog", "0.86", None))
        self.label_15.setText(_translate("optimize_bowers_Dialog", "Vmax:", None))
        self.draw_unloading_Button.setText(_translate("optimize_bowers_Dialog", "Draw", None))
        self.clear_unloading_Button.setText(_translate("optimize_bowers_Dialog", "Clear", None))

