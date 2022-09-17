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
        self.ui.pushButton.clicked.connect(self.btnClicked)

        # Кнопки, добавляющие операторы в строку
        self.ui.pushButton_and.clicked.connect(lambda: self.add_sign("∩"))
        self.ui.pushButton_or.clicked.connect(lambda: self.add_sign("∪"))
        self.ui.pushButton_diff.clicked.connect(lambda: self.add_sign("\\"))
        self.ui.pushButton_xor.clicked.connect(lambda: self.add_sign("∆"))

    def btnClicked(self):
        set_A = set(map(str, self.ui.textEdit_A.toPlainText().split(", ")))
        set_B = set(map(str, self.ui.textEdit_B.toPlainText().split(", ")))
        set_C = set(map(str, self.ui.textEdit_C.toPlainText().split(", ")))
        res = scripts.solve(self.ui.textEdit.toPlainText(), set_A, set_B, set_C)
        self.ui.textEdit_result.setText(str(res))

    def add_sign(self, symbol: str):
        old_text = self.ui.textEdit.toPlainText()
        self.ui.textEdit.setText(old_text + symbol)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
