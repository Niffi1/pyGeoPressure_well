# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bowers_dialog.ui'
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

class Ui_bowers_Dialog(object):
    def setupUi(self, bowers_Dialog):
        bowers_Dialog.setObjectName(_fromUtf8("bowers_Dialog"))
        bowers_Dialog.resize(708, 756)
        self.horizontalLayout = QtGui.QHBoxLayout(bowers_Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(bowers_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 180, 141, 221))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.u_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.u_lineEdit.setGeometry(QtCore.QRect(50, 80, 81, 20))
        self.u_lineEdit.setObjectName(_fromUtf8("u_lineEdit"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(10, 80, 31, 20))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.a_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.a_lineEdit.setGeometry(QtCore.QRect(50, 20, 81, 20))
        self.a_lineEdit.setObjectName(_fromUtf8("a_lineEdit"))
        self.b_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.b_lineEdit.setGeometry(QtCore.QRect(50, 40, 81, 20))
        self.b_lineEdit.setObjectName(_fromUtf8("b_lineEdit"))
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(10, 60, 31, 20))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.vmax_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.vmax_lineEdit.setGeometry(QtCore.QRect(50, 60, 81, 20))
        self.vmax_lineEdit.setObjectName(_fromUtf8("vmax_lineEdit"))
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(20, 40, 20, 20))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 20, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 100, 141, 81))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_20 = QtGui.QLabel(self.groupBox_5)
        self.label_20.setGeometry(QtCore.QRect(9, 20, 31, 20))
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.end_lineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.end_lineEdit.setGeometry(QtCore.QRect(50, 40, 81, 20))
        self.end_lineEdit.setObjectName(_fromUtf8("end_lineEdit"))
        self.buffer_lineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.buffer_lineEdit.setGeometry(QtCore.QRect(70, 60, 61, 20))
        self.buffer_lineEdit.setObjectName(_fromUtf8("buffer_lineEdit"))
        self.label_21 = QtGui.QLabel(self.groupBox_5)
        self.label_21.setGeometry(QtCore.QRect(10, 40, 31, 20))
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.start_lineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.start_lineEdit.setGeometry(QtCore.QRect(50, 20, 81, 20))
        self.start_lineEdit.setObjectName(_fromUtf8("start_lineEdit"))
        self.buffer_checkBox = QtGui.QCheckBox(self.groupBox_5)
        self.buffer_checkBox.setGeometry(QtCore.QRect(10, 60, 51, 17))
        self.buffer_checkBox.setChecked(True)
        self.buffer_checkBox.setObjectName(_fromUtf8("buffer_checkBox"))
        self.predict_Button = QtGui.QPushButton(self.groupBox_3)
        self.predict_Button.setGeometry(QtCore.QRect(60, 190, 71, 20))
        self.predict_Button.setObjectName(_fromUtf8("predict_Button"))
        self.save_param_Button = QtGui.QPushButton(self.groupBox_3)
        self.save_param_Button.setGeometry(QtCore.QRect(10, 190, 20, 20))
        self.save_param_Button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/save_as_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_param_Button.setIcon(icon)
        self.save_param_Button.setIconSize(QtCore.QSize(20, 20))
        self.save_param_Button.setFlat(True)
        self.save_param_Button.setObjectName(_fromUtf8("save_param_Button"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 400, 141, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.save_Button = QtGui.QPushButton(self.groupBox_2)
        self.save_Button.setGeometry(QtCore.QRect(120, 20, 20, 20))
        self.save_Button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/save_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_Button.setIcon(icon1)
        self.save_Button.setIconSize(QtCore.QSize(20, 20))
        self.save_Button.setFlat(True)
        self.save_Button.setObjectName(_fromUtf8("save_Button"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(0, 20, 121, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 51, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.velocity_comboBox = QtGui.QComboBox(self.groupBox)
        self.velocity_comboBox.setGeometry(QtCore.QRect(10, 70, 121, 22))
        self.velocity_comboBox.setObjectName(_fromUtf8("velocity_comboBox"))
        self.well_comboBox = QtGui.QComboBox(self.groupBox)
        self.well_comboBox.setGeometry(QtCore.QRect(10, 20, 121, 22))
        self.well_comboBox.setObjectName(_fromUtf8("well_comboBox"))
        self.obp_comboBox = QtGui.QComboBox(self.groupBox)
        self.obp_comboBox.setGeometry(QtCore.QRect(10, 110, 121, 22))
        self.obp_comboBox.setObjectName(_fromUtf8("obp_comboBox"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 51, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 130, 61, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.param_comboBox = QtGui.QComboBox(self.groupBox)
        self.param_comboBox.setGeometry(QtCore.QRect(10, 150, 121, 22))
        self.param_comboBox.setObjectName(_fromUtf8("param_comboBox"))
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_9 = QtGui.QGroupBox(bowers_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox_9.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.pres_listWidget = QtGui.QListWidget(self.groupBox_9)
        self.pres_listWidget.setGeometry(QtCore.QRect(10, 290, 121, 161))
        self.pres_listWidget.setObjectName(_fromUtf8("pres_listWidget"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_9)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 60, 141, 221))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.plot_horizon_Button = QtGui.QPushButton(self.groupBox_4)
        self.plot_horizon_Button.setGeometry(QtCore.QRect(60, 190, 65, 20))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/layer_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plot_horizon_Button.setIcon(icon2)
        self.plot_horizon_Button.setObjectName(_fromUtf8("plot_horizon_Button"))
        self.horizon_listWidget = QtGui.QListWidget(self.groupBox_4)
        self.horizon_listWidget.setGeometry(QtCore.QRect(10, 20, 121, 171))
        self.horizon_listWidget.setProperty("isWrapping", True)
        self.horizon_listWidget.setObjectName(_fromUtf8("horizon_listWidget"))
        self.litho_checkBox = QtGui.QCheckBox(self.groupBox_9)
        self.litho_checkBox.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.litho_checkBox.setChecked(True)
        self.litho_checkBox.setObjectName(_fromUtf8("litho_checkBox"))
        self.hydro_checkBox = QtGui.QCheckBox(self.groupBox_9)
        self.hydro_checkBox.setGeometry(QtCore.QRect(10, 40, 81, 17))
        self.hydro_checkBox.setChecked(True)
        self.hydro_checkBox.setObjectName(_fromUtf8("hydro_checkBox"))
        self.horizontalLayout.addWidget(self.groupBox_9)

        self.retranslateUi(bowers_Dialog)
        QtCore.QMetaObject.connectSlotsByName(bowers_Dialog)

    def retranslateUi(self, bowers_Dialog):
        bowers_Dialog.setWindowTitle(_translate("bowers_Dialog", "PP Bowers", None))
        self.groupBox.setTitle(_translate("bowers_Dialog", "Wells", None))
        self.groupBox_3.setTitle(_translate("bowers_Dialog", "Prediction", None))
        self.u_lineEdit.setText(_translate("bowers_Dialog", "0.86", None))
        self.label_14.setText(_translate("bowers_Dialog", "U:", None))
        self.a_lineEdit.setText(_translate("bowers_Dialog", "98", None))
        self.b_lineEdit.setText(_translate("bowers_Dialog", "0.86", None))
        self.label_15.setText(_translate("bowers_Dialog", "Vmax:", None))
        self.vmax_lineEdit.setText(_translate("bowers_Dialog", "4800", None))
        self.label_13.setText(_translate("bowers_Dialog", "B:", None))
        self.label_12.setText(_translate("bowers_Dialog", "A:", None))
        self.groupBox_5.setTitle(_translate("bowers_Dialog", "Unloading", None))
        self.label_20.setText(_translate("bowers_Dialog", "start:", None))
        self.end_lineEdit.setText(_translate("bowers_Dialog", "3500", None))
        self.buffer_lineEdit.setText(_translate("bowers_Dialog", "0", None))
        self.label_21.setText(_translate("bowers_Dialog", "end:", None))
        self.start_lineEdit.setText(_translate("bowers_Dialog", "3000", None))
        self.buffer_checkBox.setText(_translate("bowers_Dialog", "buffer:", None))
        self.predict_Button.setText(_translate("bowers_Dialog", "Predict", None))
        self.groupBox_2.setTitle(_translate("bowers_Dialog", "Save", None))
        self.lineEdit.setText(_translate("bowers_Dialog", "_bowers", None))
        self.label_5.setText(_translate("bowers_Dialog", "Velocity:", None))
        self.label_6.setText(_translate("bowers_Dialog", "OBP:", None))
        self.label_9.setText(_translate("bowers_Dialog", "Parameters:", None))
        self.groupBox_9.setTitle(_translate("bowers_Dialog", "Plot", None))
        self.groupBox_4.setTitle(_translate("bowers_Dialog", "Horizons", None))
        self.plot_horizon_Button.setText(_translate("bowers_Dialog", "Plot", None))
        self.litho_checkBox.setText(_translate("bowers_Dialog", "Lithostatic", None))
        self.hydro_checkBox.setText(_translate("bowers_Dialog", "Hydrostatic", None))

import resources_rc
