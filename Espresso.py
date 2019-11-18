import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAbstractItemView, QTableWidgetItem


class EventsModel:
    def __init__(self):
        self.conn = sqlite3.connect('Coffee.db')
        self.cursor = self.conn.cursor()

    def get_information(self):
        return self.cursor.execute("SELECT * FROM Coffee").fetchall()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Coffee.ui', self)

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.resizeColumnsToContents()

        self.table()

    def table(self):
        self.tableWidget.setRowCount(0)
        self.a = e_model.get_information()
        print(self.a)
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e_model = EventsModel()
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())