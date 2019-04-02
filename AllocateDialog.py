import sys
from PyQt5.QtWidgets import (QDialog, QApplication, QTableWidget, QAbstractItemView,
                             QVBoxLayout, QTableWidgetItem, QPushButton,
                             QHBoxLayout, QMessageBox, QWidget)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import qdarkstyle


class AllocateDialog(QDialog):
    def __init__(self):
        super(AllocateDialog, self).__init__()
        self.resize(1200, 500)
        self.setWindowTitle('myERP——调配构成表')
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
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels(['调配基准编号', '调配区代码', '父物料号', '父物料名称',
                                                    '子物料号' , '子物料名称' , '构成数' , '配料提前期' , '供应商提前期'])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalHeaderItem(0).setFont(QFont("苏新诗柳楷繁", 11))
        self.tableWidget.horizontalHeaderItem(1).setFont(QFont("苏新诗柳楷繁", 11))
        self.tableWidget.horizontalHeaderItem(2).setFont(QFont("苏新诗柳楷繁", 11))
        self.tableWidget.horizontalHeaderItem(3).setFont(QFont("苏新诗柳楷繁", 11))
        self.tableWidget.horizontalHeaderItem(4).setFont(QFont("苏新诗柳楷繁", 11))
        self.tableWidget.horizontalHeaderItem(5).setFont(QFont("苏新诗柳楷繁", 11))
        self.tableWidget.horizontalHeaderItem(6).setFont(QFont("苏新诗柳楷繁", 11))
        self.tableWidget.horizontalHeaderItem(7).setFont(QFont("苏新诗柳楷繁", 11))
        self.tableWidget.horizontalHeaderItem(8).setFont(QFont("苏新诗柳楷繁", 11))

        self.layout.addWidget(self.tableWidget)
        self.setRows()

    def getResult(self):

        sql = "select * from allocate order by alid"

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
                Item5 = QTableWidgetItem(self.query.value(4))
                Item6 = QTableWidgetItem(self.query.value(5))
                Item7 = QTableWidgetItem(self.query.value(6))
                Item8 = QTableWidgetItem(self.query.value(7))
                Item9 = QTableWidgetItem(self.query.value(8))

                Item1.setFont(QFont("苏新诗柳楷繁", 12))
                Item2.setFont(QFont("苏新诗柳楷繁", 12))
                Item3.setFont(QFont("苏新诗柳楷繁", 12))
                Item4.setFont(QFont("苏新诗柳楷繁", 12))
                Item5.setFont(QFont("苏新诗柳楷繁", 12))
                Item6.setFont(QFont("苏新诗柳楷繁", 12))
                Item7.setFont(QFont("苏新诗柳楷繁", 12))
                Item8.setFont(QFont("苏新诗柳楷繁", 12))
                Item9.setFont(QFont("苏新诗柳楷繁", 12))

                Item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                Item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                Item3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                Item4.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                Item5.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                Item6.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                Item7.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                Item8.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                Item9.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

                self.tableWidget.setItem(i, 0, Item1)
                self.tableWidget.setItem(i, 1, Item2)
                self.tableWidget.setItem(i, 2, Item3)
                self.tableWidget.setItem(i, 3, Item4)
                self.tableWidget.setItem(i, 4, Item5)
                self.tableWidget.setItem(i, 5, Item6)
                self.tableWidget.setItem(i, 6, Item7)
                self.tableWidget.setItem(i, 7, Item8)
                self.tableWidget.setItem(i, 8, Item9)
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    allocatedialog = AllocateDialog()
    allocatedialog.show()
    sys.exit(app.exec_())
