# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nct_dialog.ui'
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

class Ui_nct_Dialog(object):
    def setupUi(self, nct_Dialog):
        nct_Dialog.setObjectName(_fromUtf8("nct_Dialog"))
        nct_Dialog.resize(686, 752)
        self.horizontalLayout = QtGui.QHBoxLayout(nct_Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(nct_Dialog)
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
        self.sm_log_comboBox = QtGui.QComboBox(self.groupBox)
        self.sm_log_comboBox.setGeometry(QtCore.QRect(10, 120, 111, 20))
        self.sm_log_comboBox.setObjectName(_fromUtf8("sm_log_comboBox"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 81, 20))
        self.label_6.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.sh_log_comboBox = QtGui.QComboBox(self.groupBox)
        self.sh_log_comboBox.setGeometry(QtCore.QRect(10, 170, 111, 20))
        self.sh_log_comboBox.setObjectName(_fromUtf8("sh_log_comboBox"))
        self.shale_checkBox = QtGui.QCheckBox(self.groupBox)
        self.shale_checkBox.setGeometry(QtCore.QRect(10, 150, 91, 17))
        self.shale_checkBox.setObjectName(_fromUtf8("shale_checkBox"))
        self.horizon_listWidget = QtGui.QListWidget(self.groupBox)
        self.horizon_listWidget.setGeometry(QtCore.QRect(10, 340, 121, 171))
        self.horizon_listWidget.setProperty("isWrapping", True)
        self.horizon_listWidget.setObjectName(_fromUtf8("horizon_listWidget"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 320, 61, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.plot_Button = QtGui.QPushButton(self.groupBox)
        self.plot_Button.setGeometry(QtCore.QRect(60, 200, 65, 23))
        self.plot_Button.setObjectName(_fromUtf8("plot_Button"))
        self.plot_horizon_Button = QtGui.QPushButton(self.groupBox)
        self.plot_horizon_Button.setGeometry(QtCore.QRect(60, 520, 65, 23))
        self.plot_horizon_Button.setObjectName(_fromUtf8("plot_horizon_Button"))
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(nct_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.add_Button = QtGui.QPushButton(self.groupBox_2)
        self.add_Button.setGeometry(QtCore.QRect(100, 570, 31, 20))
        self.add_Button.setObjectName(_fromUtf8("add_Button"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 550, 101, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 320, 61, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.copy_Button = QtGui.QPushButton(self.groupBox_2)
        self.copy_Button.setGeometry(QtCore.QRect(50, 520, 31, 23))
        self.copy_Button.setObjectName(_fromUtf8("copy_Button"))
        self.new_name_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.new_name_lineEdit.setGeometry(QtCore.QRect(10, 570, 81, 20))
        self.new_name_lineEdit.setObjectName(_fromUtf8("new_name_lineEdit"))
        self.delete_Button = QtGui.QPushButton(self.groupBox_2)
        self.delete_Button.setGeometry(QtCore.QRect(10, 520, 31, 23))
        self.delete_Button.setObjectName(_fromUtf8("delete_Button"))
        self.draw_Button = QtGui.QPushButton(self.groupBox_2)
        self.draw_Button.setGeometry(QtCore.QRect(0, 70, 65, 23))
        self.draw_Button.setObjectName(_fromUtf8("draw_Button"))
        self.fit_Button = QtGui.QPushButton(self.groupBox_2)
        self.fit_Button.setGeometry(QtCore.QRect(0, 150, 65, 23))
        self.fit_Button.setObjectName(_fromUtf8("fit_Button"))
        self.extrapolate_Button = QtGui.QPushButton(self.groupBox_2)
        self.extrapolate_Button.setGeometry(QtCore.QRect(70, 70, 65, 23))
        self.extrapolate_Button.setObjectName(_fromUtf8("extrapolate_Button"))
        self.clear_Button = QtGui.QPushButton(self.groupBox_2)
        self.clear_Button.setGeometry(QtCore.QRect(70, 150, 65, 23))
        self.clear_Button.setObjectName(_fromUtf8("clear_Button"))
        self.a_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.a_lineEdit.setGeometry(QtCore.QRect(50, 20, 81, 20))
        self.a_lineEdit.setObjectName(_fromUtf8("a_lineEdit"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 31, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 31, 20))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.b_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.b_lineEdit.setGeometry(QtCore.QRect(50, 40, 81, 20))
        self.b_lineEdit.setObjectName(_fromUtf8("b_lineEdit"))
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 100, 31, 20))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.start_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.start_lineEdit.setGeometry(QtCore.QRect(50, 100, 81, 20))
        self.start_lineEdit.setObjectName(_fromUtf8("start_lineEdit"))
        self.label_15 = QtGui.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(10, 120, 31, 20))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.end_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.end_lineEdit.setGeometry(QtCore.QRect(50, 120, 81, 20))
        self.end_lineEdit.setObjectName(_fromUtf8("end_lineEdit"))
        self.two_points_checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.two_points_checkBox.setGeometry(QtCore.QRect(10, 190, 121, 20))
        self.two_points_checkBox.setObjectName(_fromUtf8("two_points_checkBox"))
        self.two_points_groupBox = QtGui.QGroupBox(self.groupBox_2)
        self.two_points_groupBox.setGeometry(QtCore.QRect(0, 210, 141, 101))
        self.two_points_groupBox.setTitle(_fromUtf8(""))
        self.two_points_groupBox.setObjectName(_fromUtf8("two_points_groupBox"))
        self.point1_radioButton = QtGui.QRadioButton(self.two_points_groupBox)
        self.point1_radioButton.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.point1_radioButton.setChecked(True)
        self.point1_radioButton.setObjectName(_fromUtf8("point1_radioButton"))
        self.point2_radioButton = QtGui.QRadioButton(self.two_points_groupBox)
        self.point2_radioButton.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.point2_radioButton.setObjectName(_fromUtf8("point2_radioButton"))
        self.x_point1_lineEdit = QtGui.QLineEdit(self.two_points_groupBox)
        self.x_point1_lineEdit.setGeometry(QtCore.QRect(10, 20, 60, 20))
        self.x_point1_lineEdit.setObjectName(_fromUtf8("x_point1_lineEdit"))
        self.y_point1_lineEdit = QtGui.QLineEdit(self.two_points_groupBox)
        self.y_point1_lineEdit.setGeometry(QtCore.QRect(70, 20, 60, 20))
        self.y_point1_lineEdit.setObjectName(_fromUtf8("y_point1_lineEdit"))
        self.y_point2_lineEdit = QtGui.QLineEdit(self.two_points_groupBox)
        self.y_point2_lineEdit.setGeometry(QtCore.QRect(70, 60, 60, 20))
        self.y_point2_lineEdit.setObjectName(_fromUtf8("y_point2_lineEdit"))
        self.x_point2_lineEdit = QtGui.QLineEdit(self.two_points_groupBox)
        self.x_point2_lineEdit.setGeometry(QtCore.QRect(10, 60, 60, 20))
        self.x_point2_lineEdit.setObjectName(_fromUtf8("x_point2_lineEdit"))
        self.pick_checkBox = QtGui.QCheckBox(self.two_points_groupBox)
        self.pick_checkBox.setGeometry(QtCore.QRect(10, 80, 81, 20))
        self.pick_checkBox.setObjectName(_fromUtf8("pick_checkBox"))
        self.nct_tableWidget = QtGui.QTableWidget(self.groupBox_2)
        self.nct_tableWidget.setGeometry(QtCore.QRect(10, 340, 121, 171))
        self.nct_tableWidget.setObjectName(_fromUtf8("nct_tableWidget"))
        self.nct_tableWidget.setColumnCount(3)
        self.nct_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.nct_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.nct_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.nct_tableWidget.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(nct_Dialog)
        QtCore.QMetaObject.connectSlotsByName(nct_Dialog)

    def retranslateUi(self, nct_Dialog):
        nct_Dialog.setWindowTitle(_translate("nct_Dialog", "NCT Velocity", None))
        self.groupBox.setTitle(_translate("nct_Dialog", "Data", None))
        self.label.setText(_translate("nct_Dialog", "Well", None))
        self.label_2.setText(_translate("nct_Dialog", "Log", None))
        self.label_6.setText(_translate("nct_Dialog", "Smoothed Log", None))
        self.shale_checkBox.setText(_translate("nct_Dialog", "Shale Volume", None))
        self.label_11.setText(_translate("nct_Dialog", "Horizons:", None))
        self.plot_Button.setText(_translate("nct_Dialog", "Plot", None))
        self.plot_horizon_Button.setText(_translate("nct_Dialog", "Plot", None))
        self.groupBox_2.setTitle(_translate("nct_Dialog", "NCT", None))
        self.add_Button.setText(_translate("nct_Dialog", "Add", None))
        self.label_4.setText(_translate("nct_Dialog", "Save current result", None))
        self.label_3.setText(_translate("nct_Dialog", "Saved NCT", None))
        self.copy_Button.setText(_translate("nct_Dialog", "Copy", None))
        self.new_name_lineEdit.setToolTip(_translate("nct_Dialog", "new parameter name", None))
        self.new_name_lineEdit.setText(_translate("nct_Dialog", "nct_", None))
        self.delete_Button.setText(_translate("nct_Dialog", "Del", None))
        self.draw_Button.setText(_translate("nct_Dialog", "Draw", None))
        self.fit_Button.setText(_translate("nct_Dialog", "Fit", None))
        self.extrapolate_Button.setText(_translate("nct_Dialog", "Extrapolate", None))
        self.clear_Button.setText(_translate("nct_Dialog", "Clear", None))
        self.label_12.setText(_translate("nct_Dialog", "a:", None))
        self.label_13.setText(_translate("nct_Dialog", "b:", None))
        self.label_14.setText(_translate("nct_Dialog", "start:", None))
        self.label_15.setText(_translate("nct_Dialog", "end:", None))
        self.two_points_checkBox.setText(_translate("nct_Dialog", "Use 2 points methods", None))
        self.point1_radioButton.setText(_translate("nct_Dialog", "Point 1", None))
        self.point2_radioButton.setText(_translate("nct_Dialog", "Point 2", None))
        self.pick_checkBox.setText(_translate("nct_Dialog", "Pick Points", None))
        item = self.nct_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("nct_Dialog", "key", None))
        item = self.nct_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("nct_Dialog", "a", None))
        item = self.nct_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("nct_Dialog", "b", None))

