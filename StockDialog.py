import sys
from PyQt5.QtWidgets import (QDialog, QApplication, QTableWidget, QAbstractItemView,
                             QVBoxLayout, QTableWidgetItem, QPushButton,
                             QHBoxLayout, QMessageBox, QWidget)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import qdarkstyle


class StockDialog(QDialog):
    def __init__(self):
        super(StockDialog, self).__init__()
        self.resize(560, 500)
        self.setWindowTitle('myERP——库存表')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.petCount = 0
        self.initUI()

    def initUI(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('./db/myERP.db')
        self.db.open()
        self.query = QSqlQuery()
        self.getResult()

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.petCount)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['物料号', '物料名称', '工序库存', '资材库存'])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeaderItem(0).setFont(QFont("苏新诗柳楷繁", 12))
        self.tableWidget.horizontalHeaderItem(1).setFont(QFont("苏新诗柳楷繁", 12))
        self.tableWidget.horizontalHeaderItem(2).setFont(QFont("苏新诗柳楷繁", 12))
        self.tableWidget.horizontalHeaderItem(3).setFont(QFont("苏新诗柳楷繁", 12))

        self.layout.addWidget(self.tableWidget)
        self.setRows()

    def getResult(self):

        sql = "select * from stock"

        self.query.exec_(sql)
        self.petCount = 0;
        while (self.query.next()):
            self.petCount += 1;

        self.query.exec_(sql)

    def setRows(self):
        font = QFont()
        font.setPixelSize(14)
        for i in range(self.petCount):
            if (self.query.next()):
                Item1 = QTableWidgetItem(self.query.value(0))
                Item2 = QTableWidgetItem(self.query.value(1))
                Item3 = QTableWidgetItem(self.query.value(2))
                Item4 = QTableWidgetItem(self.query.value(3))

                Item1.setFont(QFont("苏新诗柳楷繁", 12))
                Item2.setFont(QFont("苏新诗柳楷繁", 12))
                Item3.setFont(QFont("苏新诗柳楷繁", 12))
                Item4.setFont(QFont("苏新诗柳楷繁", 12))

                Item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                Item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                Item3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                Item4.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                self.tableWidget.setItem(i, 0, Item1)
                self.tableWidget.setItem(i, 1, Item2)
                self.tableWidget.setItem(i, 2, Item3)
                self.tableWidget.setItem(i, 3, Item4)
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    stockdialog = StockDialog()
    stockdialog.show()
    sys.exit(app.exec_())
