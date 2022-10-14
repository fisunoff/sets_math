from PyQt5 import QtWidgets, QtCore
import sys
from test1 import Ui_DockWidget
import scripts


class MyWindow(QtWidgets.QDockWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_DockWidget()
        self.ui.setupUi(self)

        # кнопка РЕШИТЬ
        self.ui.solve_btn.clicked.connect(self.btn_clicked)

        # Кнопки, добавляющие операторы в строку
        self.ui.pushButton_and.clicked.connect(lambda: self.add_sign("∩"))
        self.ui.pushButton_or.clicked.connect(lambda: self.add_sign("∪"))
        self.ui.pushButton_diff.clicked.connect(lambda: self.add_sign("\\"))
        self.ui.pushButton_xor.clicked.connect(lambda: self.add_sign("∆"))
        self.ui.pushButton_addition.clicked.connect(lambda: self.add_sign("¯"))
        self.ui.pushButton_cartesian.clicked.connect(lambda: self.add_sign("X"))
        self.ui.pushButton_powerset.clicked.connect(lambda: self.add_sign("powerset()"))

    def init_sets(self):
        str_A = self.ui.textEdit_A.toPlainText()
        str_B = self.ui.textEdit_B.toPlainText()
        str_C = self.ui.textEdit_C.toPlainText()
        self.set_A = set(map(str, str_A.split(", "))) if str_A else set()
        self.set_B = set(map(str, str_B.split(", "))) if str_B else set()
        self.set_C = set(map(str, str_C.split(", "))) if str_C else set()

    def btn_clicked(self):
        self.init_sets()
        res = scripts.solve(self.ui.textEdit.toPlainText(), self.set_A, self.set_B, self.set_C)
        self.ui.textEdit_result.setText(str(res[1]))
        if res[0] == "error":
            self.ui.textEdit_result.setStyleSheet("background-color: rgb(255, 76, 91);\n")
        else:
            self.ui.textEdit_result.setStyleSheet("background-color: rgb(152, 251, 152);\n")

    def add_sign(self, symbol: str):
        old_text = self.ui.textEdit.toPlainText()
        self.ui.textEdit.insertPlainText(symbol)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
