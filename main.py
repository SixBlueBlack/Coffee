import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QTableWidgetItem, QDialog
from addEditCoffeeForm import Ui_Dialog
from main1 import Ui_MainWindow


class EventsModel:
    def __init__(self):
        self.conn = sqlite3.connect('data/Coffee.db')
        self.cursor = self.conn.cursor()

    def get_information(self):
        return self.cursor.execute("SELECT * FROM Coffee").fetchall()

    def add_event(self, kind, degree_of_roasting, typ, taste, price, amount):
        self.cursor.execute(
            "INSERT INTO Coffee(kind, degree_of_roasting, type, taste, price, amount) VALUES (?, ?, ?, ?, ?, ?)",
            (kind, degree_of_roasting, typ, taste, price, amount))
        self.conn.commit()

    def update_event(self, id, kind, degree_of_roasting, typ, taste, price, amount):
        self.cursor.execute(
            "UPDATE Coffee SET kind = ?, degree_of_roasting = ?, type = ?, "
            "taste = ?, price = ?, amount = ? WHERE id = ?",
            (kind, degree_of_roasting, typ, taste, price, amount, id))
        self.conn.commit()

    def clear(self):
        self.cursor.execute("DELETE from Coffee")
        self.conn.commit()


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update = False
        self.a = []

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.resizeColumnsToContents()

        self.pushButton.clicked.connect(self.add_event)
        self.pushButton_2.clicked.connect(self.update_event)
        self.pushButton_3.clicked.connect(self.clear)

        self.table()

    def add_event(self):
        self.update = False
        event_win.title.setText('')
        event_win.description.setText('')
        event_win.textEdit.setText('')
        event_win.lineEdit.setText('')
        event_win.lineEdit_2.setText('')
        event_win.radioButton_2.setChecked(False)
        event_win.exec()

    def update_event(self):
        self.a = []
        if not self.tableWidget.currentItem():
            return
        for i in range(7):
            self.a.append(self.tableWidget.item(self.tableWidget.currentRow(), i).text())
        print(self.a)
        self.update = True
        event_win.title.setText(self.a[1])
        event_win.description.setText(self.a[4])
        event_win.textEdit.setText(self.a[2])
        event_win.lineEdit.setText(self.a[5])
        event_win.lineEdit_2.setText(self.a[6])
        event_win.radioButton_2.setChecked(True)
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
        self.tableWidget.sortItems(5)

    def clear(self):
        e_model.clear()
        self.table()


class SetEventWin(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.radioButton_2.setChecked(True)

        self.buttonBox.accepted.connect(self.write_event)

    def write_event(self):
        if self.radioButton.isChecked() == True:
            a = 'зерновой'
        else:
            a = 'молотый'
        if ex.update:
            e_model.update_event(ex.a[0], self.title.text(), self.textEdit.toPlainText(), a,
                                 self.description.toPlainText(),
                                 self.lineEdit.text(), self.lineEdit_2.text())
        else:
            e_model.add_event(self.title.text(), self.textEdit.toPlainText(), a, self.description.toPlainText(),
                              self.lineEdit.text(), self.lineEdit_2.text())
        ex.table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e_model = EventsModel()
    ex = MyWidget()
    event_win = SetEventWin()
    ex.show()
    sys.exit(app.exec_())
