import sys
import traceback
import time
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtGui, uic
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from GetBaseInfo1 import def1


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

    # bind functions
    def search_button_clicked_0(self):
        stock_code_edit_0 = self.stock_code_edit_0.toPlainText()
        current_date_edit_0 = str(
            self.current_date_edit_0.date().toPyDate())
        res_0 = def1(stock_code_edit_0, current_date_edit_0)
        ConsoleLog("股票代码：{}\t日期：{}".format(
            stock_code_edit_0, current_date_edit_0), True)
        self.search_num_0.display(res_0.shape[0])

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
