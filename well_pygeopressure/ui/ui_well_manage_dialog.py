# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'well_manage_dialog.ui'
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

class Ui_well_manage_Dialog(object):
    def setupUi(self, well_manage_Dialog):
        well_manage_Dialog.setObjectName(_fromUtf8("well_manage_Dialog"))
        well_manage_Dialog.resize(644, 655)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/data_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        well_manage_Dialog.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(well_manage_Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.wells_listWidget = QtGui.QListWidget(well_manage_Dialog)
        self.wells_listWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.wells_listWidget.setObjectName(_fromUtf8("wells_listWidget"))
        self.horizontalLayout.addWidget(self.wells_listWidget)
        self.groupBox = QtGui.QGroupBox(well_manage_Dialog)
        self.groupBox.setMinimumSize(QtCore.QSize(25, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.rename_well_Button = QtGui.QPushButton(self.groupBox)
        self.rename_well_Button.setGeometry(QtCore.QRect(0, 10, 25, 25))
        self.rename_well_Button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/rename_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rename_well_Button.setIcon(icon1)
        self.rename_well_Button.setIconSize(QtCore.QSize(20, 20))
        self.rename_well_Button.setFlat(True)
        self.rename_well_Button.setObjectName(_fromUtf8("rename_well_Button"))
        self.delete_well_Button = QtGui.QPushButton(self.groupBox)
        self.delete_well_Button.setGeometry(QtCore.QRect(0, 40, 25, 25))
        self.delete_well_Button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/delete_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_well_Button.setIcon(icon2)
        self.delete_well_Button.setIconSize(QtCore.QSize(20, 20))
        self.delete_well_Button.setFlat(True)
        self.delete_well_Button.setObjectName(_fromUtf8("delete_well_Button"))
        self.import_well_Button = QtGui.QPushButton(self.groupBox)
        self.import_well_Button.setGeometry(QtCore.QRect(0, 70, 25, 25))
        self.import_well_Button.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/import_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_well_Button.setIcon(icon3)
        self.import_well_Button.setIconSize(QtCore.QSize(20, 20))
        self.import_well_Button.setFlat(True)
        self.import_well_Button.setObjectName(_fromUtf8("import_well_Button"))
        self.layer_well_Button = QtGui.QPushButton(self.groupBox)
        self.layer_well_Button.setGeometry(QtCore.QRect(0, 100, 25, 25))
        self.layer_well_Button.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/layer_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.layer_well_Button.setIcon(icon4)
        self.layer_well_Button.setIconSize(QtCore.QSize(20, 20))
        self.layer_well_Button.setFlat(True)
        self.layer_well_Button.setObjectName(_fromUtf8("layer_well_Button"))
        self.horizontalLayout.addWidget(self.groupBox)
        self.logs_listWidget = QtGui.QListWidget(well_manage_Dialog)
        self.logs_listWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.logs_listWidget.setObjectName(_fromUtf8("logs_listWidget"))
        self.horizontalLayout.addWidget(self.logs_listWidget)
        self.groupBox_3 = QtGui.QGroupBox(well_manage_Dialog)
        self.groupBox_3.setMinimumSize(QtCore.QSize(25, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.view_log_Button = QtGui.QPushButton(self.groupBox_3)
        self.view_log_Button.setGeometry(QtCore.QRect(0, 100, 25, 25))
        self.view_log_Button.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/view_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_log_Button.setIcon(icon5)
        self.view_log_Button.setIconSize(QtCore.QSize(20, 20))
        self.view_log_Button.setFlat(True)
        self.view_log_Button.setObjectName(_fromUtf8("view_log_Button"))
        self.delete_log_Button = QtGui.QPushButton(self.groupBox_3)
        self.delete_log_Button.setGeometry(QtCore.QRect(0, 40, 25, 25))
        self.delete_log_Button.setText(_fromUtf8(""))
        self.delete_log_Button.setIcon(icon2)
        self.delete_log_Button.setIconSize(QtCore.QSize(20, 20))
        self.delete_log_Button.setFlat(True)
        self.delete_log_Button.setObjectName(_fromUtf8("delete_log_Button"))
        self.rename_log_Button = QtGui.QPushButton(self.groupBox_3)
        self.rename_log_Button.setGeometry(QtCore.QRect(0, 10, 25, 25))
        self.rename_log_Button.setText(_fromUtf8(""))
        self.rename_log_Button.setIcon(icon1)
        self.rename_log_Button.setIconSize(QtCore.QSize(20, 20))
        self.rename_log_Button.setFlat(True)
        self.rename_log_Button.setObjectName(_fromUtf8("rename_log_Button"))
        self.import_log_Button = QtGui.QPushButton(self.groupBox_3)
        self.import_log_Button.setGeometry(QtCore.QRect(0, 70, 25, 25))
        self.import_log_Button.setText(_fromUtf8(""))
        self.import_log_Button.setIcon(icon3)
        self.import_log_Button.setIconSize(QtCore.QSize(20, 20))
        self.import_log_Button.setFlat(True)
        self.import_log_Button.setObjectName(_fromUtf8("import_log_Button"))
        self.edit_log_Button = QtGui.QPushButton(self.groupBox_3)
        self.edit_log_Button.setGeometry(QtCore.QRect(0, 130, 25, 25))
        self.edit_log_Button.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/edit_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_log_Button.setIcon(icon6)
        self.edit_log_Button.setIconSize(QtCore.QSize(20, 20))
        self.edit_log_Button.setFlat(True)
        self.edit_log_Button.setObjectName(_fromUtf8("edit_log_Button"))
        self.create_log_Button = QtGui.QPushButton(self.groupBox_3)
        self.create_log_Button.setGeometry(QtCore.QRect(0, 160, 25, 25))
        self.create_log_Button.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/create_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.create_log_Button.setIcon(icon7)
        self.create_log_Button.setIconSize(QtCore.QSize(20, 20))
        self.create_log_Button.setFlat(True)
        self.create_log_Button.setObjectName(_fromUtf8("create_log_Button"))
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.info_textEdit = QtGui.QTextEdit(well_manage_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_textEdit.sizePolicy().hasHeightForWidth())
        self.info_textEdit.setSizePolicy(sizePolicy)
        self.info_textEdit.setMinimumSize(QtCore.QSize(0, 150))
        self.info_textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.info_textEdit.setObjectName(_fromUtf8("info_textEdit"))
        self.horizontalLayout_3.addWidget(self.info_textEdit)
        self.saved_info_tableWidget = QtGui.QTableWidget(well_manage_Dialog)
        self.saved_info_tableWidget.setMinimumSize(QtCore.QSize(0, 150))
        self.saved_info_tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.saved_info_tableWidget.setObjectName(_fromUtf8("saved_info_tableWidget"))
        self.saved_info_tableWidget.setColumnCount(2)
        self.saved_info_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.saved_info_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.saved_info_tableWidget.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_3.addWidget(self.saved_info_tableWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(well_manage_Dialog)
        QtCore.QMetaObject.connectSlotsByName(well_manage_Dialog)

    def retranslateUi(self, well_manage_Dialog):
        well_manage_Dialog.setWindowTitle(_translate("well_manage_Dialog", "Well Management", None))
        self.rename_well_Button.setToolTip(_translate("well_manage_Dialog", "Rename Well", None))
        self.delete_well_Button.setToolTip(_translate("well_manage_Dialog", "Delete Well", None))
        self.import_well_Button.setToolTip(_translate("well_manage_Dialog", "Import Well", None))
        self.layer_well_Button.setToolTip(_translate("well_manage_Dialog", "Well Layer Markers", None))
        self.view_log_Button.setToolTip(_translate("well_manage_Dialog", "View Log curve", None))
        self.delete_log_Button.setToolTip(_translate("well_manage_Dialog", "Delete", None))
        self.rename_log_Button.setToolTip(_translate("well_manage_Dialog", "Rename", None))
        self.import_log_Button.setToolTip(_translate("well_manage_Dialog", "Import Log", None))
        self.edit_log_Button.setToolTip(_translate("well_manage_Dialog", "Edit Log data", None))
        self.create_log_Button.setToolTip(_translate("well_manage_Dialog", "Create new Log curve", None))
        item = self.saved_info_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("well_manage_Dialog", "keys", None))
        item = self.saved_info_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("well_manage_Dialog", "value", None))

import resources_rc
