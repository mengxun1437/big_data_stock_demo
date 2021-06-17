import sys
import traceback
import time
import pandas as pd
from PyQt5 import QtCore, QtWidgets, QtGui, uic
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from GetBaseInfo1 import def1
from GetBaseInfo2 import def2
from GetDerivativeInfo import def3
from GetCorrelationInfo import def4
from GetVisualization import def5, drawPic
from Xlwings import def6
from Excel import def7, drawPicAndSaveFIle


# ui文件
qtCreatorFile = "main.ui"

# load UI
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


# 信号槽，用于std out
class EmittingStr(QtCore.QObject):
    text_written = QtCore.pyqtSignal(str)  # 定义一个str的信号

    def write(self, text):
        self.text_written.emit(str(text))
        loop = QEventLoop()
        QTimer.singleShot(1, loop.quit)
        loop.exec_()

# exception handle


class PyQT4_unhandled_exception(Exception):
    def __init__(self, *args):
        super(PyQT4_unhandled_exception, self).__init__(*args)


def unhandled_exception(type, value, tb):
    if isinstance(value, PyQT4_unhandled_exception):
        QMessageBox.critical(
            value.args[0], "Error", value.args[1], QMessageBox.Ok)
    else:
        traceback.print_exception(type, value, tb)


def ConsoleLog(text, logTime=False):
    if logTime:
        print("")
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print(str(text))

    # build table model


def build_table_model(df):
    rows = df.shape[0] - 1
    columns = df.shape[1]
    model = QStandardItemModel(rows, columns)
    model.setHorizontalHeaderLabels(df.columns.values.tolist())

    for row in range(rows):
        for column in range(columns):
            item = QStandardItem(str(df.iloc[row + 1, column]))
            model.setItem(row, column, item)
    return model


# build app
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        sys.excepthook = unhandled_exception
        sys.stdout = EmittingStr(text_written=self.output_written)
        sys.stderr = EmittingStr(text_written=self.output_written)

        # def1
        self.search_button_0.clicked.connect(self.search_button_clicked_0)
        self.search_button_1.clicked.connect(self.search_button_clicked_1)
        self.search_button_2.clicked.connect(self.search_button_clicked_2)
        self.search_button_3.clicked.connect(self.search_button_clicked_3)
        self.search_button_4.clicked.connect(self.search_button_clicked_4)
        self.save_button_5.clicked.connect(self.save_button_clicked_5)
        self.search_button_6.clicked.connect(self.search_button_clicked_6)

    # bind functions

    def search_button_clicked_0(self):
        stock_code_edit_0 = self.stock_code_edit_0.toPlainText()
        current_date_edit_0 = str(
            self.current_date_edit_0.date().toPyDate())
        res_0 = def1(stock_code_edit_0, current_date_edit_0)
        ConsoleLog("股票代码：{}\t日期：{}".format(
            stock_code_edit_0, current_date_edit_0), True)
        ConsoleLog("记录数：行 {} 列 {}".format(res_0.shape[0] - 1, res_0.shape[1]))
        self.search_num_0.display(res_0.shape[0] - 1)
        self.total_vol_0.display(res_0.volume.sum())
        # table
        model_0 = build_table_model(res_0)
        self.search_table_result_0.setModel(model_0)

    def search_button_clicked_1(self):
        stock_code_edit_1 = self.stock_code_edit_1.toPlainText()
        stock_name_edit_1 = self.stock_name_edit_1.toPlainText()
        start_date_edit_1 = str(
            self.start_date_edit_1.date().toPyDate())
        end_date_edit_1 = str(
            self.end_date_edit_1.date().toPyDate())
        res_1 = def2(stock_code_edit_1, stock_name_edit_1,
                     start_date_edit_1, end_date_edit_1)
        ConsoleLog("股票代码：{}\t股票名称：{}\t开始日期：{}\t结束日期：{}".format(
            stock_code_edit_1, stock_name_edit_1, start_date_edit_1, end_date_edit_1), True)
        ConsoleLog("记录数：行 {} 列 {}".format(res_1.shape[0] - 1, res_1.shape[1]))
        self.search_num_1.display(res_1.shape[0] - 1)
        # print(res_1)
        # table
        model_1 = build_table_model(res_1)
        self.search_table_result_1.setModel(model_1)

    def search_button_clicked_2(self):
        stock_code_edit_2 = self.stock_code_edit_2.toPlainText()
        stock_name_edit_2 = self.stock_name_edit_2.toPlainText()
        start_date_edit_2 = str(
            self.start_date_edit_2.date().toPyDate())
        end_date_edit_2 = str(
            self.end_date_edit_2.date().toPyDate())
        res_2 = def3(stock_code_edit_2, stock_name_edit_2,
                     start_date_edit_2, end_date_edit_2)
        ConsoleLog("股票代码：{}\t股票名称：{}\t开始日期：{}\t结束日期：{}".format(
            stock_code_edit_2, stock_name_edit_2, start_date_edit_2, end_date_edit_2), True)
        ConsoleLog("记录数：行 {} 列 {}".format(res_2.shape[0] - 1, res_2.shape[1]))
        self.search_num_2.display(res_2.shape[0] - 1)
        # table
        model_2 = build_table_model(res_2)
        self.search_table_result_2.setModel(model_2)

    def search_button_clicked_3(self):
        stock_code_edit_3 = self.stock_code_edit_3.toPlainText()
        stock_name_edit_3 = self.stock_name_edit_3.toPlainText()
        start_date_edit_3 = str(
            self.start_date_edit_3.date().toPyDate())
        end_date_edit_3 = str(
            self.end_date_edit_3.date().toPyDate())
        tmp_res = def4(stock_code_edit_3, stock_name_edit_3,
                       start_date_edit_3, end_date_edit_3)
        res_3 = tmp_res['stock_table']
        res_corr1 = tmp_res['corr1']
        res_corr2 = tmp_res['corr2']
        ConsoleLog("股票代码：{}\t股票名称：{}\t开始日期：{}\t结束日期：{}".format(
            stock_code_edit_3, stock_name_edit_3, start_date_edit_3, end_date_edit_3), True)
        ConsoleLog("记录数：行 {} 列 {}".format(res_3.shape[0] - 1, res_3.shape[1]))
        self.search_num_3.display(res_3.shape[0] - 1)
        self.correlation_num_3_r1.display(res_corr1[0])
        self.correlation_num_3_r2.display(res_corr2[0])
        self.correlation_num_3_p1.display(res_corr1[1])
        self.correlation_num_3_p2.display(res_corr2[1])
        # table
        model_3 = build_table_model(res_3)
        self.search_table_result_3.setModel(model_3)

    def search_button_clicked_4(self):
        stock_code_edit_4 = self.stock_code_edit_4.toPlainText()
        stock_name_edit_4 = self.stock_name_edit_4.toPlainText()
        start_date_edit_4 = str(
            self.start_date_edit_4.date().toPyDate())
        end_date_edit_4 = str(
            self.end_date_edit_4.date().toPyDate())
        res_4 = def5(stock_code_edit_4, stock_name_edit_4,
                     start_date_edit_4, end_date_edit_4)
        ConsoleLog("股票代码：{}\t股票名称：{}\t开始日期：{}\t结束日期：{}".format(
            stock_code_edit_4, stock_name_edit_4, start_date_edit_4, end_date_edit_4), True)
        ConsoleLog("记录数：行 {} 列 {}".format(res_4.shape[0] - 1, res_4.shape[1]))
        self.search_num_4.display(res_4.shape[0] - 1)
        # table
        model_4 = build_table_model(res_4)
        self.search_table_result_4.setModel(model_4)

        # 绘制
        drawPic(stock_name_edit_4, res_4)

    def save_button_clicked_5(self):
        sheet_name_edit_5 = self.sheet_name_edit_5.toPlainText()
        a1_value_edit_5 = self.a1_value_edit_5.toPlainText()
        file_name_edit_5 = self.file_name_edit_5.toPlainText()
        file_path_edit_5 = QFileDialog.getExistingDirectory(
            self, "请选择保存路径", "d:/")
        res_5 = def6(sheet_name_edit_5, a1_value_edit_5,
                     file_name_edit_5, file_path_edit_5)
        ConsoleLog("sheet值：{}\tA1单元格值：{}\t文件名：{}\t文件路径：{}".format(
            sheet_name_edit_5, a1_value_edit_5, file_name_edit_5, file_path_edit_5), True)
        ConsoleLog("保存结果：{}".format("成功" if res_5 else "失败"))
        self.save_status_5.display(res_5)

    def search_button_clicked_6(self):
        stock_code_edit_6 = self.stock_code_edit_6.toPlainText()
        stock_name_edit_6 = self.stock_name_edit_6.toPlainText()
        start_date_edit_6 = str(
            self.start_date_edit_6.date().toPyDate())
        end_date_edit_6 = str(
            self.end_date_edit_6.date().toPyDate())
        res_6 = def5(stock_code_edit_6, stock_name_edit_6,
                     start_date_edit_6, end_date_edit_6)
        ConsoleLog("股票代码：{}\t股票名称：{}\t开始日期：{}\t结束日期：{}".format(
            stock_code_edit_6, stock_name_edit_6, start_date_edit_6, end_date_edit_6), True)
        ConsoleLog("记录数：行 {} 列 {}".format(res_6.shape[0] - 1, res_6.shape[1]))
        self.search_num_6.display(res_6.shape[0] - 1)
        # table
        model_6 = build_table_model(res_6)
        self.search_table_result_6.setModel(model_6)

        # 绘制
        suc = drawPicAndSaveFIle(stock_name_edit_6, res_6)
        self.save_status_6.display(suc)
        ConsoleLog("保存结果：{}\t保存路径：{}".format(
            "成功" if suc else "失败", "D:/股票分析.xlsx"))

    # utils

    def output_written(self, text):
        cursor = self.console_log_info.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.console_log_info.setTextCursor(cursor)
        self.console_log_info.ensureCursorVisible()


# main run the gui
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
