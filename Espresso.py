import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QTableWidgetItem, QDialog


class EventsModel:
    def __init__(self):
        self.conn = sqlite3.connect('Coffee.db')
        self.cursor = self.conn.cursor()

    def get_information(self):
        return self.cursor.execute("SELECT * FROM Coffee").fetchall()

    def add_event(self, kind, degree_of_roasting, typ, taste, price, amount):
        self.cursor.execute(
            "INSERT INTO Coffee(kind, degree_of_roasting, type, taste, price, amount) VALUES (?, ?, ?, ?, ?, ?)",
            (kind, degree_of_roasting, typ, taste, price, amount))
        self.conn.commit()
        ex.table()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Coffee.ui', self)

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.resizeColumnsToContents()

        self.pushButton.clicked.connect(self.add_event)
        self.pushButton_2.clicked.connect(self.update_event)

        self.table()

    def add_event(self):
        self.update = False
        event_win.exec()

    def update_event(self):
        self.update = True
        event_win.exec()

    def table(self):
        self.tableWidget.setRowCount(0)
        self.a = e_model.get_information()
        if self.a:
            for elem in self.a:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(elem[0])))
                self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(elem[1]))
                self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(elem[2]))
                self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(elem[3]))
                self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(elem[4]))
                self.tableWidget.setItem(rowPosition, 5, QTableWidgetItem(str(elem[5])))
                self.tableWidget.setItem(rowPosition, 6, QTableWidgetItem(str(elem[6])))

                self.tableWidget.resizeColumnsToContents()


class SetEventWin(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.radioButton_2.setChecked(True)

        self.buttonBox.accepted.connect(self.write_event)

    def write_event(self):
        if ex.update:
            self.update_event()
            return
        if self.radioButton.isChecked() == True:
            a = 'зерновой'
        else:
            a = 'молотый'
        e_model.add_event(self.title.text(), self.textEdit.toPlainText(), a, self.description.toPlainText(),
                          self.lineEdit.text(), self.lineEdit_2.text())

        self.title.setText('')
        self.description.setText('')
        self.textEdit.setText('')
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.radioButton_2.setChecked(True)

    def update_event(self):
        if self.radioButton.isChecked() == True:
            a = 'зерновой'
        else:
            a = 'молотый'
        e_model.add_event(self.title.text(), self.textEdit.toPlainText(), a, self.description.toPlainText(),
                          self.lineEdit.text(), self.lineEdit_2.text())

        self.title.setText('')
        self.description.setText('')
        self.textEdit.setText('')
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.radioButton_2.setChecked(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e_model = EventsModel()
    ex = MyWidget()
    event_win = SetEventWin()
    ex.show()
    sys.exit(app.exec_())
