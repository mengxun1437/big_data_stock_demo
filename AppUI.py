# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AppUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BigData(object):
    def setupUi(self, BigData):
        BigData.setObjectName("BigData")
        BigData.setEnabled(True)
        BigData.resize(1517, 896)
        self.centralwidget = QtWidgets.QWidget(BigData)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setEnabled(True)
        self.tabs.setGeometry(QtCore.QRect(40, 60, 1001, 811))
        self.tabs.setLocale(QtCore.QLocale(
            QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.tabs.setObjectName("tabs")
        self._14_2_1_1 = QtWidgets.QWidget()
        self._14_2_1_1.setObjectName("_14_2_1_1")
        self.groupBox = QtWidgets.QGroupBox(self._14_2_1_1)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 951, 61))
        self.groupBox.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox.setObjectName("groupBox")
        self.stock_code_edit_0 = QtWidgets.QTextEdit(self.groupBox)
        self.stock_code_edit_0.setGeometry(QtCore.QRect(70, 20, 131, 30))
        self.stock_code_edit_0.setObjectName("stock_code_edit_0")
        self.stock_code_label_0 = QtWidgets.QLabel(self.groupBox)
        self.stock_code_label_0.setGeometry(QtCore.QRect(10, 25, 71, 16))
        self.stock_code_label_0.setObjectName("stock_code_label_0")
        self.current_date_edit_0 = QtWidgets.QDateEdit(self.groupBox)
        self.current_date_edit_0.setGeometry(QtCore.QRect(280, 20, 110, 30))
        self.current_date_edit_0.setObjectName("current_date_edit_0")
        self.current_date_label_0 = QtWidgets.QLabel(self.groupBox)
        self.current_date_label_0.setGeometry(QtCore.QRect(230, 25, 41, 16))
        self.current_date_label_0.setObjectName("current_date_label_0")
        self.search_button_0 = QtWidgets.QPushButton(self.groupBox)
        self.search_button_0.setGeometry(QtCore.QRect(820, 20, 88, 30))
        self.search_button_0.setObjectName("search_button_0")
        self.groupBox_2 = QtWidgets.QGroupBox(self._14_2_1_1)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 90, 951, 681))
        self.groupBox_2.setObjectName("groupBox_2")
        self.search_tip_label_0 = QtWidgets.QLabel(self.groupBox_2)
        self.search_tip_label_0.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.search_tip_label_0.setObjectName("search_tip_label_0")
        self.search_num_0 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.search_num_0.setGeometry(QtCore.QRect(80, 25, 81, 25))
        self.search_num_0.setDigitCount(6)
        self.search_num_0.setObjectName("search_num_0")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 60, 72, 15))
        self.label.setObjectName("label")
        self.search_table_result_0 = QtWidgets.QTableView(self.groupBox_2)
        self.search_table_result_0.setGeometry(QtCore.QRect(10, 80, 931, 591))
        self.search_table_result_0.setObjectName("search_table_result_0")
        self.total_vol_0 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.total_vol_0.setGeometry(QtCore.QRect(260, 25, 81, 25))
        self.total_vol_0.setDigitCount(6)
        self.total_vol_0.setObjectName("total_vol_0")
        self.search_tip_label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.search_tip_label_3.setGeometry(QtCore.QRect(200, 30, 72, 15))
        self.search_tip_label_3.setObjectName("search_tip_label_3")
        self.tabs.addTab(self._14_2_1_1, "")
        self._14_2_1_2 = QtWidgets.QWidget()
        self._14_2_1_2.setObjectName("_14_2_1_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self._14_2_1_2)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 10, 951, 61))
        self.groupBox_4.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_4.setObjectName("groupBox_4")
        self.stock_code_edit_1 = QtWidgets.QTextEdit(self.groupBox_4)
        self.stock_code_edit_1.setGeometry(QtCore.QRect(70, 20, 81, 30))
        self.stock_code_edit_1.setObjectName("stock_code_edit_1")
        self.stock_code_label_1 = QtWidgets.QLabel(self.groupBox_4)
        self.stock_code_label_1.setGeometry(QtCore.QRect(10, 25, 61, 16))
        self.stock_code_label_1.setObjectName("stock_code_label_1")
        self.start_date_edit_1 = QtWidgets.QDateEdit(self.groupBox_4)
        self.start_date_edit_1.setGeometry(QtCore.QRect(390, 20, 110, 30))
        self.start_date_edit_1.setObjectName("start_date_edit_1")
        self.current_date_label_1 = QtWidgets.QLabel(self.groupBox_4)
        self.current_date_label_1.setGeometry(QtCore.QRect(330, 25, 61, 16))
        self.current_date_label_1.setObjectName("current_date_label_1")
        self.search_button_1 = QtWidgets.QPushButton(self.groupBox_4)
        self.search_button_1.setGeometry(QtCore.QRect(820, 20, 88, 30))
        self.search_button_1.setObjectName("search_button_1")
        self.stock_code_label_1_1 = QtWidgets.QLabel(self.groupBox_4)
        self.stock_code_label_1_1.setGeometry(QtCore.QRect(170, 25, 61, 16))
        self.stock_code_label_1_1.setObjectName("stock_code_label_1_1")
        self.stock_name_edit_1 = QtWidgets.QTextEdit(self.groupBox_4)
        self.stock_name_edit_1.setGeometry(QtCore.QRect(230, 20, 81, 30))
        self.stock_name_edit_1.setObjectName("stock_name_edit_1")
        self.current_date_label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.current_date_label_2.setGeometry(QtCore.QRect(520, 25, 61, 16))
        self.current_date_label_2.setObjectName("current_date_label_2")
        self.end_date_edit_1 = QtWidgets.QDateEdit(self.groupBox_4)
        self.end_date_edit_1.setGeometry(QtCore.QRect(580, 20, 110, 30))
        self.end_date_edit_1.setObjectName("end_date_edit_1")
        self.groupBox_6 = QtWidgets.QGroupBox(self._14_2_1_2)
        self.groupBox_6.setEnabled(True)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 90, 951, 681))
        self.groupBox_6.setObjectName("groupBox_6")
        self.search_tip_label_1 = QtWidgets.QLabel(self.groupBox_6)
        self.search_tip_label_1.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.search_tip_label_1.setObjectName("search_tip_label_1")
        self.search_num_1 = QtWidgets.QLCDNumber(self.groupBox_6)
        self.search_num_1.setGeometry(QtCore.QRect(80, 25, 81, 25))
        self.search_num_1.setDigitCount(6)
        self.search_num_1.setObjectName("search_num_1")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 72, 15))
        self.label_2.setObjectName("label_2")
        self.search_table_result_1 = QtWidgets.QTableView(self.groupBox_6)
        self.search_table_result_1.setGeometry(QtCore.QRect(10, 80, 931, 591))
        self.search_table_result_1.setObjectName("search_table_result_1")
        self.tabs.addTab(self._14_2_1_2, "")
        self._14_2_2 = QtWidgets.QWidget()
        self._14_2_2.setObjectName("_14_2_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self._14_2_2)
        self.groupBox_7.setEnabled(True)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 90, 951, 681))
        self.groupBox_7.setObjectName("groupBox_7")
        self.search_tip_label_2 = QtWidgets.QLabel(self.groupBox_7)
        self.search_tip_label_2.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.search_tip_label_2.setObjectName("search_tip_label_2")
        self.search_num_2 = QtWidgets.QLCDNumber(self.groupBox_7)
        self.search_num_2.setGeometry(QtCore.QRect(80, 25, 81, 25))
        self.search_num_2.setDigitCount(6)
        self.search_num_2.setObjectName("search_num_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_7)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 72, 15))
        self.label_3.setObjectName("label_3")
        self.search_table_result_2 = QtWidgets.QTableView(self.groupBox_7)
        self.search_table_result_2.setGeometry(QtCore.QRect(10, 80, 931, 591))
        self.search_table_result_2.setObjectName("search_table_result_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self._14_2_2)
        self.groupBox_5.setEnabled(True)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 10, 951, 61))
        self.groupBox_5.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_5.setObjectName("groupBox_5")
        self.stock_code_edit_2 = QtWidgets.QTextEdit(self.groupBox_5)
        self.stock_code_edit_2.setGeometry(QtCore.QRect(70, 20, 81, 30))
        self.stock_code_edit_2.setObjectName("stock_code_edit_2")
        self.stock_code_label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.stock_code_label_2.setGeometry(QtCore.QRect(10, 25, 61, 16))
        self.stock_code_label_2.setObjectName("stock_code_label_2")
        self.start_date_edit_2 = QtWidgets.QDateEdit(self.groupBox_5)
        self.start_date_edit_2.setGeometry(QtCore.QRect(390, 20, 110, 30))
        self.start_date_edit_2.setObjectName("start_date_edit_2")
        self.current_date_label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.current_date_label_3.setGeometry(QtCore.QRect(330, 25, 61, 16))
        self.current_date_label_3.setObjectName("current_date_label_3")
        self.search_button_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.search_button_2.setGeometry(QtCore.QRect(820, 20, 88, 30))
        self.search_button_2.setObjectName("search_button_2")
        self.stock_code_label_1_2 = QtWidgets.QLabel(self.groupBox_5)
        self.stock_code_label_1_2.setGeometry(QtCore.QRect(170, 25, 61, 16))
        self.stock_code_label_1_2.setObjectName("stock_code_label_1_2")
        self.stock_name_edit_2 = QtWidgets.QTextEdit(self.groupBox_5)
        self.stock_name_edit_2.setGeometry(QtCore.QRect(230, 20, 81, 30))
        self.stock_name_edit_2.setObjectName("stock_name_edit_2")
        self.current_date_label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.current_date_label_4.setGeometry(QtCore.QRect(520, 25, 61, 16))
        self.current_date_label_4.setObjectName("current_date_label_4")
        self.end_date_edit_2 = QtWidgets.QDateEdit(self.groupBox_5)
        self.end_date_edit_2.setGeometry(QtCore.QRect(580, 20, 110, 30))
        self.end_date_edit_2.setObjectName("end_date_edit_2")
        self.tabs.addTab(self._14_2_2, "")
        self._14_2_3 = QtWidgets.QWidget()
        self._14_2_3.setObjectName("_14_2_3")
        self.groupBox_8 = QtWidgets.QGroupBox(self._14_2_3)
        self.groupBox_8.setEnabled(True)
        self.groupBox_8.setGeometry(QtCore.QRect(20, 90, 951, 681))
        self.groupBox_8.setObjectName("groupBox_8")
        self.search_tip_label_4 = QtWidgets.QLabel(self.groupBox_8)
        self.search_tip_label_4.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.search_tip_label_4.setObjectName("search_tip_label_4")
        self.search_num_3 = QtWidgets.QLCDNumber(self.groupBox_8)
        self.search_num_3.setGeometry(QtCore.QRect(80, 25, 81, 25))
        self.search_num_3.setDigitCount(6)
        self.search_num_3.setObjectName("search_num_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_8)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 72, 15))
        self.label_4.setObjectName("label_4")
        self.search_table_result_3 = QtWidgets.QTableView(self.groupBox_8)
        self.search_table_result_3.setGeometry(QtCore.QRect(10, 80, 931, 591))
        self.search_table_result_3.setObjectName("search_table_result_3")
        self.search_tip_label_5 = QtWidgets.QLabel(self.groupBox_8)
        self.search_tip_label_5.setGeometry(QtCore.QRect(180, 30, 61, 16))
        self.search_tip_label_5.setObjectName("search_tip_label_5")
        self.correlation_num_3_r1 = QtWidgets.QLCDNumber(self.groupBox_8)
        self.correlation_num_3_r1.setGeometry(QtCore.QRect(250, 25, 81, 25))
        self.correlation_num_3_r1.setDigitCount(6)
        self.correlation_num_3_r1.setObjectName("correlation_num_3_r1")
        self.search_tip_label_6 = QtWidgets.QLabel(self.groupBox_8)
        self.search_tip_label_6.setGeometry(QtCore.QRect(540, 30, 71, 16))
        self.search_tip_label_6.setObjectName("search_tip_label_6")
        self.correlation_num_3_r2 = QtWidgets.QLCDNumber(self.groupBox_8)
        self.correlation_num_3_r2.setGeometry(QtCore.QRect(620, 25, 81, 25))
        self.correlation_num_3_r2.setDigitCount(6)
        self.correlation_num_3_r2.setObjectName("correlation_num_3_r2")
        self.search_tip_label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.search_tip_label_10.setGeometry(QtCore.QRect(350, 30, 81, 16))
        self.search_tip_label_10.setObjectName("search_tip_label_10")
        self.correlation_num_3_p1 = QtWidgets.QLCDNumber(self.groupBox_8)
        self.correlation_num_3_p1.setGeometry(QtCore.QRect(440, 25, 81, 25))
        self.correlation_num_3_p1.setDigitCount(6)
        self.correlation_num_3_p1.setObjectName("correlation_num_3_p1")
        self.search_tip_label_11 = QtWidgets.QLabel(self.groupBox_8)
        self.search_tip_label_11.setGeometry(QtCore.QRect(720, 30, 81, 16))
        self.search_tip_label_11.setObjectName("search_tip_label_11")
        self.correlation_num_3_p2 = QtWidgets.QLCDNumber(self.groupBox_8)
        self.correlation_num_3_p2.setGeometry(QtCore.QRect(810, 25, 81, 25))
        self.correlation_num_3_p2.setDigitCount(6)
        self.correlation_num_3_p2.setObjectName("correlation_num_3_p2")
        self.groupBox_9 = QtWidgets.QGroupBox(self._14_2_3)
        self.groupBox_9.setEnabled(True)
        self.groupBox_9.setGeometry(QtCore.QRect(20, 10, 951, 61))
        self.groupBox_9.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_9.setObjectName("groupBox_9")
        self.stock_code_edit_3 = QtWidgets.QTextEdit(self.groupBox_9)
        self.stock_code_edit_3.setGeometry(QtCore.QRect(70, 20, 81, 30))
        self.stock_code_edit_3.setObjectName("stock_code_edit_3")
        self.stock_code_label_3 = QtWidgets.QLabel(self.groupBox_9)
        self.stock_code_label_3.setGeometry(QtCore.QRect(10, 25, 61, 16))
        self.stock_code_label_3.setObjectName("stock_code_label_3")
        self.start_date_edit_3 = QtWidgets.QDateEdit(self.groupBox_9)
        self.start_date_edit_3.setGeometry(QtCore.QRect(390, 20, 110, 30))
        self.start_date_edit_3.setObjectName("start_date_edit_3")
        self.current_date_label_5 = QtWidgets.QLabel(self.groupBox_9)
        self.current_date_label_5.setGeometry(QtCore.QRect(330, 25, 61, 16))
        self.current_date_label_5.setObjectName("current_date_label_5")
        self.search_button_3 = QtWidgets.QPushButton(self.groupBox_9)
        self.search_button_3.setGeometry(QtCore.QRect(820, 20, 88, 30))
        self.search_button_3.setObjectName("search_button_3")
        self.stock_code_label_1_3 = QtWidgets.QLabel(self.groupBox_9)
        self.stock_code_label_1_3.setGeometry(QtCore.QRect(170, 25, 61, 16))
        self.stock_code_label_1_3.setObjectName("stock_code_label_1_3")
        self.stock_name_edit_3 = QtWidgets.QTextEdit(self.groupBox_9)
        self.stock_name_edit_3.setGeometry(QtCore.QRect(230, 20, 81, 30))
        self.stock_name_edit_3.setObjectName("stock_name_edit_3")
        self.current_date_label_6 = QtWidgets.QLabel(self.groupBox_9)
        self.current_date_label_6.setGeometry(QtCore.QRect(520, 25, 61, 16))
        self.current_date_label_6.setObjectName("current_date_label_6")
        self.end_date_edit_3 = QtWidgets.QDateEdit(self.groupBox_9)
        self.end_date_edit_3.setGeometry(QtCore.QRect(580, 20, 110, 30))
        self.end_date_edit_3.setObjectName("end_date_edit_3")
        self.tabs.addTab(self._14_2_3, "")
        self._14_3 = QtWidgets.QWidget()
        self._14_3.setObjectName("_14_3")
        self.groupBox_11 = QtWidgets.QGroupBox(self._14_3)
        self.groupBox_11.setEnabled(True)
        self.groupBox_11.setGeometry(QtCore.QRect(20, 90, 951, 681))
        self.groupBox_11.setObjectName("groupBox_11")
        self.search_tip_label_12 = QtWidgets.QLabel(self.groupBox_11)
        self.search_tip_label_12.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.search_tip_label_12.setObjectName("search_tip_label_12")
        self.search_num_4 = QtWidgets.QLCDNumber(self.groupBox_11)
        self.search_num_4.setGeometry(QtCore.QRect(80, 25, 81, 25))
        self.search_num_4.setDigitCount(6)
        self.search_num_4.setObjectName("search_num_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_11)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 72, 15))
        self.label_6.setObjectName("label_6")
        self.search_table_result_4 = QtWidgets.QTableView(self.groupBox_11)
        self.search_table_result_4.setGeometry(QtCore.QRect(10, 80, 931, 591))
        self.search_table_result_4.setObjectName("search_table_result_4")
        self.groupBox_10 = QtWidgets.QGroupBox(self._14_3)
        self.groupBox_10.setEnabled(True)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 10, 951, 61))
        self.groupBox_10.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_10.setObjectName("groupBox_10")
        self.stock_code_edit_4 = QtWidgets.QTextEdit(self.groupBox_10)
        self.stock_code_edit_4.setGeometry(QtCore.QRect(70, 20, 81, 30))
        self.stock_code_edit_4.setObjectName("stock_code_edit_4")
        self.stock_code_label_4 = QtWidgets.QLabel(self.groupBox_10)
        self.stock_code_label_4.setGeometry(QtCore.QRect(10, 25, 61, 16))
        self.stock_code_label_4.setObjectName("stock_code_label_4")
        self.start_date_edit_4 = QtWidgets.QDateEdit(self.groupBox_10)
        self.start_date_edit_4.setGeometry(QtCore.QRect(390, 20, 110, 30))
        self.start_date_edit_4.setObjectName("start_date_edit_4")
        self.current_date_label_7 = QtWidgets.QLabel(self.groupBox_10)
        self.current_date_label_7.setGeometry(QtCore.QRect(330, 25, 61, 16))
        self.current_date_label_7.setObjectName("current_date_label_7")
        self.search_button_4 = QtWidgets.QPushButton(self.groupBox_10)
        self.search_button_4.setGeometry(QtCore.QRect(820, 20, 88, 30))
        self.search_button_4.setObjectName("search_button_4")
        self.stock_code_label_1_4 = QtWidgets.QLabel(self.groupBox_10)
        self.stock_code_label_1_4.setGeometry(QtCore.QRect(170, 25, 61, 16))
        self.stock_code_label_1_4.setObjectName("stock_code_label_1_4")
        self.stock_name_edit_4 = QtWidgets.QTextEdit(self.groupBox_10)
        self.stock_name_edit_4.setGeometry(QtCore.QRect(230, 20, 81, 30))
        self.stock_name_edit_4.setObjectName("stock_name_edit_4")
        self.current_date_label_8 = QtWidgets.QLabel(self.groupBox_10)
        self.current_date_label_8.setGeometry(QtCore.QRect(520, 25, 61, 16))
        self.current_date_label_8.setObjectName("current_date_label_8")
        self.end_date_edit_4 = QtWidgets.QDateEdit(self.groupBox_10)
        self.end_date_edit_4.setGeometry(QtCore.QRect(580, 20, 110, 30))
        self.end_date_edit_4.setObjectName("end_date_edit_4")
        self.tabs.addTab(self._14_3, "")
        self._14_4_1 = QtWidgets.QWidget()
        self._14_4_1.setObjectName("_14_4_1")
        self.groupBox_12 = QtWidgets.QGroupBox(self._14_4_1)
        self.groupBox_12.setEnabled(True)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 90, 951, 681))
        self.groupBox_12.setObjectName("groupBox_12")
        self.search_tip_label_13 = QtWidgets.QLabel(self.groupBox_12)
        self.search_tip_label_13.setGeometry(QtCore.QRect(20, 30, 191, 16))
        self.search_tip_label_13.setObjectName("search_tip_label_13")
        self.save_status_5 = QtWidgets.QLCDNumber(self.groupBox_12)
        self.save_status_5.setGeometry(QtCore.QRect(210, 25, 31, 25))
        self.save_status_5.setSmallDecimalPoint(True)
        self.save_status_5.setDigitCount(1)
        self.save_status_5.setMode(QtWidgets.QLCDNumber.Dec)
        self.save_status_5.setProperty("value", 0.0)
        self.save_status_5.setProperty("intValue", 0)
        self.save_status_5.setObjectName("save_status_5")
        self.groupBox_13 = QtWidgets.QGroupBox(self._14_4_1)
        self.groupBox_13.setEnabled(True)
        self.groupBox_13.setGeometry(QtCore.QRect(20, 10, 951, 61))
        self.groupBox_13.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_13.setObjectName("groupBox_13")
        self.sheet_name_edit_5 = QtWidgets.QTextEdit(self.groupBox_13)
        self.sheet_name_edit_5.setGeometry(QtCore.QRect(70, 20, 81, 30))
        self.sheet_name_edit_5.setObjectName("sheet_name_edit_5")
        self.stock_code_label_5 = QtWidgets.QLabel(self.groupBox_13)
        self.stock_code_label_5.setGeometry(QtCore.QRect(10, 25, 61, 16))
        self.stock_code_label_5.setObjectName("stock_code_label_5")
        self.save_button_5 = QtWidgets.QPushButton(self.groupBox_13)
        self.save_button_5.setGeometry(QtCore.QRect(820, 20, 88, 30))
        self.save_button_5.setObjectName("save_button_5")
        self.stock_code_label_1_5 = QtWidgets.QLabel(self.groupBox_13)
        self.stock_code_label_1_5.setGeometry(QtCore.QRect(170, 25, 41, 16))
        self.stock_code_label_1_5.setObjectName("stock_code_label_1_5")
        self.a1_value_edit_5 = QtWidgets.QTextEdit(self.groupBox_13)
        self.a1_value_edit_5.setGeometry(QtCore.QRect(210, 20, 81, 30))
        self.a1_value_edit_5.setObjectName("a1_value_edit_5")
        self.stock_code_label_1_6 = QtWidgets.QLabel(self.groupBox_13)
        self.stock_code_label_1_6.setGeometry(QtCore.QRect(310, 25, 51, 16))
        self.stock_code_label_1_6.setObjectName("stock_code_label_1_6")
        self.file_name_edit_5 = QtWidgets.QTextEdit(self.groupBox_13)
        self.file_name_edit_5.setGeometry(QtCore.QRect(360, 20, 81, 30))
        self.file_name_edit_5.setObjectName("file_name_edit_5")
        self.tabs.addTab(self._14_4_1, "")
        self._14_4_2 = QtWidgets.QWidget()
        self._14_4_2.setObjectName("_14_4_2")
        self.groupBox_14 = QtWidgets.QGroupBox(self._14_4_2)
        self.groupBox_14.setEnabled(True)
        self.groupBox_14.setGeometry(QtCore.QRect(20, 90, 951, 681))
        self.groupBox_14.setObjectName("groupBox_14")
        self.search_tip_label_14 = QtWidgets.QLabel(self.groupBox_14)
        self.search_tip_label_14.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.search_tip_label_14.setObjectName("search_tip_label_14")
        self.search_num_6 = QtWidgets.QLCDNumber(self.groupBox_14)
        self.search_num_6.setGeometry(QtCore.QRect(80, 25, 81, 25))
        self.search_num_6.setDigitCount(6)
        self.search_num_6.setObjectName("search_num_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_14)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 72, 15))
        self.label_7.setObjectName("label_7")
        self.search_table_result_6 = QtWidgets.QTableView(self.groupBox_14)
        self.search_table_result_6.setGeometry(QtCore.QRect(10, 80, 931, 591))
        self.search_table_result_6.setObjectName("search_table_result_6")
        self.search_tip_label_15 = QtWidgets.QLabel(self.groupBox_14)
        self.search_tip_label_15.setGeometry(QtCore.QRect(180, 30, 191, 16))
        self.search_tip_label_15.setObjectName("search_tip_label_15")
        self.save_status_6 = QtWidgets.QLCDNumber(self.groupBox_14)
        self.save_status_6.setGeometry(QtCore.QRect(370, 25, 31, 25))
        self.save_status_6.setSmallDecimalPoint(True)
        self.save_status_6.setDigitCount(1)
        self.save_status_6.setMode(QtWidgets.QLCDNumber.Dec)
        self.save_status_6.setProperty("value", 0.0)
        self.save_status_6.setProperty("intValue", 0)
        self.save_status_6.setObjectName("save_status_6")
        self.groupBox_15 = QtWidgets.QGroupBox(self._14_4_2)
        self.groupBox_15.setEnabled(True)
        self.groupBox_15.setGeometry(QtCore.QRect(20, 10, 951, 61))
        self.groupBox_15.setLocale(QtCore.QLocale(
            QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_15.setObjectName("groupBox_15")
        self.stock_code_edit_6 = QtWidgets.QTextEdit(self.groupBox_15)
        self.stock_code_edit_6.setGeometry(QtCore.QRect(70, 20, 81, 30))
        self.stock_code_edit_6.setObjectName("stock_code_edit_6")
        self.stock_code_label_6 = QtWidgets.QLabel(self.groupBox_15)
        self.stock_code_label_6.setGeometry(QtCore.QRect(10, 25, 61, 16))
        self.stock_code_label_6.setObjectName("stock_code_label_6")
        self.start_date_edit_6 = QtWidgets.QDateEdit(self.groupBox_15)
        self.start_date_edit_6.setGeometry(QtCore.QRect(390, 20, 110, 30))
        self.start_date_edit_6.setObjectName("start_date_edit_6")
        self.current_date_label_9 = QtWidgets.QLabel(self.groupBox_15)
        self.current_date_label_9.setGeometry(QtCore.QRect(330, 25, 61, 16))
        self.current_date_label_9.setObjectName("current_date_label_9")
        self.search_button_6 = QtWidgets.QPushButton(self.groupBox_15)
        self.search_button_6.setGeometry(QtCore.QRect(787, 20, 121, 30))
        self.search_button_6.setObjectName("search_button_6")
        self.stock_code_label_1_7 = QtWidgets.QLabel(self.groupBox_15)
        self.stock_code_label_1_7.setGeometry(QtCore.QRect(170, 25, 61, 16))
        self.stock_code_label_1_7.setObjectName("stock_code_label_1_7")
        self.stock_name_edit_6 = QtWidgets.QTextEdit(self.groupBox_15)
        self.stock_name_edit_6.setGeometry(QtCore.QRect(230, 20, 81, 30))
        self.stock_name_edit_6.setObjectName("stock_name_edit_6")
        self.current_date_label_10 = QtWidgets.QLabel(self.groupBox_15)
        self.current_date_label_10.setGeometry(QtCore.QRect(520, 25, 61, 16))
        self.current_date_label_10.setObjectName("current_date_label_10")
        self.end_date_edit_6 = QtWidgets.QDateEdit(self.groupBox_15)
        self.end_date_edit_6.setGeometry(QtCore.QRect(580, 20, 110, 30))
        self.end_date_edit_6.setObjectName("end_date_edit_6")
        self.tabs.addTab(self._14_4_2, "")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setEnabled(True)
        self.title_label.setGeometry(QtCore.QRect(400, 30, 161, 16))
        self.title_label.setObjectName("title_label")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1060, 70, 431, 801))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.console_log_info = QtWidgets.QTextEdit(self.groupBox_3)
        self.console_log_info.setGeometry(QtCore.QRect(10, 20, 411, 761))
        self.console_log_info.setObjectName("console_log_info")
        BigData.setCentralWidget(self.centralwidget)

        self.retranslateUi(BigData)
        self.tabs.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(BigData)

    def retranslateUi(self, BigData):
        _translate = QtCore.QCoreApplication.translate
        BigData.setWindowTitle(_translate("BigData", "大数据-大作业-GUI版"))
        self.groupBox.setTitle(_translate("BigData", "操作"))
        self.stock_code_label_0.setText(_translate("BigData", "股票代码:"))
        self.current_date_label_0.setText(_translate("BigData", "日期:"))
        self.search_button_0.setText(_translate("BigData", "查询"))
        self.groupBox_2.setTitle(_translate("BigData", "结果"))
        self.search_tip_label_0.setText(_translate("BigData", "查询总数:"))
        self.label.setText(_translate("BigData", "查询结果："))
        self.search_tip_label_3.setText(_translate("BigData", "总成交量："))
        self.tabs.setTabText(self.tabs.indexOf(
            self._14_2_1_1), _translate("BigData", "14.2.1-1"))
        self.groupBox_4.setTitle(_translate("BigData", "操作"))
        self.stock_code_label_1.setText(_translate("BigData", "股票代码:"))
        self.current_date_label_1.setText(_translate("BigData", "开始日期："))
        self.search_button_1.setText(_translate("BigData", "查询"))
        self.stock_code_label_1_1.setText(_translate("BigData", "股票名称："))
        self.current_date_label_2.setText(_translate("BigData", "结束日期："))
        self.groupBox_6.setTitle(_translate("BigData", "结果"))
        self.search_tip_label_1.setText(_translate("BigData", "查询总数:"))
        self.label_2.setText(_translate("BigData", "查询结果："))
        self.tabs.setTabText(self.tabs.indexOf(
            self._14_2_1_2), _translate("BigData", "14.2.1-2"))
        self.groupBox_7.setTitle(_translate("BigData", "结果"))
        self.search_tip_label_2.setText(_translate("BigData", "查询总数:"))
        self.label_3.setText(_translate("BigData", "查询结果："))
        self.groupBox_5.setTitle(_translate("BigData", "操作"))
        self.stock_code_label_2.setText(_translate("BigData", "股票代码:"))
        self.current_date_label_3.setText(_translate("BigData", "开始日期："))
        self.search_button_2.setText(_translate("BigData", "查询"))
        self.stock_code_label_1_2.setText(_translate("BigData", "股票名称："))
        self.current_date_label_4.setText(_translate("BigData", "结束日期："))
        self.tabs.setTabText(self.tabs.indexOf(
            self._14_2_2), _translate("BigData", "14.2.2"))
        self.groupBox_8.setTitle(_translate("BigData", "结果"))
        self.search_tip_label_4.setText(_translate("BigData", "查询总数:"))
        self.label_4.setText(_translate("BigData", "查询结果："))
        self.search_tip_label_5.setText(_translate("BigData", "相关系数r1："))
        self.search_tip_label_6.setText(_translate("BigData", "相关系数r2："))
        self.search_tip_label_10.setText(_translate("BigData", "显著性水平p1:"))
        self.search_tip_label_11.setText(_translate("BigData", "显著性水平p2:"))
        self.groupBox_9.setTitle(_translate("BigData", "操作"))
        self.stock_code_label_3.setText(_translate("BigData", "股票代码:"))
        self.current_date_label_5.setText(_translate("BigData", "开始日期："))
        self.search_button_3.setText(_translate("BigData", "查询"))
        self.stock_code_label_1_3.setText(_translate("BigData", "股票名称："))
        self.current_date_label_6.setText(_translate("BigData", "结束日期："))
        self.tabs.setTabText(self.tabs.indexOf(
            self._14_2_3), _translate("BigData", "14.2.3"))
        self.groupBox_11.setTitle(_translate("BigData", "结果"))
        self.search_tip_label_12.setText(_translate("BigData", "查询总数:"))
        self.label_6.setText(_translate("BigData", "查询结果："))
        self.groupBox_10.setTitle(_translate("BigData", "操作"))
        self.stock_code_label_4.setText(_translate("BigData", "股票代码:"))
        self.current_date_label_7.setText(_translate("BigData", "开始日期："))
        self.search_button_4.setText(_translate("BigData", "查询并绘制"))
        self.stock_code_label_1_4.setText(_translate("BigData", "股票名称："))
        self.current_date_label_8.setText(_translate("BigData", "结束日期："))
        self.tabs.setTabText(self.tabs.indexOf(self._14_3),
                             _translate("BigData", "14.2.4 - 14.3"))
        self.groupBox_12.setTitle(_translate("BigData", "结果"))
        self.search_tip_label_13.setText(
            _translate("BigData", "保存结果(1代表成功/0代表失败):"))
        self.groupBox_13.setTitle(_translate("BigData", "操作"))
        self.stock_code_label_5.setText(_translate("BigData", "sheet名："))
        self.save_button_5.setText(_translate("BigData", "保存"))
        self.stock_code_label_1_5.setText(_translate("BigData", "A1值："))
        self.stock_code_label_1_6.setText(_translate("BigData", "文件名："))
        self.tabs.setTabText(self.tabs.indexOf(
            self._14_4_1), _translate("BigData", "14.4.1"))
        self.groupBox_14.setTitle(_translate("BigData", "结果"))
        self.search_tip_label_14.setText(_translate("BigData", "查询总数:"))
        self.label_7.setText(_translate("BigData", "查询结果："))
        self.search_tip_label_15.setText(
            _translate("BigData", "保存结果(1代表成功/0代表失败):"))
        self.groupBox_15.setTitle(_translate("BigData", "操作"))
        self.stock_code_label_6.setText(_translate("BigData", "股票代码:"))
        self.current_date_label_9.setText(_translate("BigData", "开始日期："))
        self.search_button_6.setText(_translate("BigData", "查询 绘制 保存"))
        self.stock_code_label_1_7.setText(_translate("BigData", "股票名称："))
        self.current_date_label_10.setText(_translate("BigData", "结束日期："))
        self.tabs.setTabText(self.tabs.indexOf(
            self._14_4_2), _translate("BigData", "14.4.2"))
        self.title_label.setText(_translate("BigData", "大数据期末大作业GUI版"))
        self.groupBox_3.setTitle(_translate("BigData", "控制台日志"))