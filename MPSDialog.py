import sys
from PyQt5.QtWidgets import (QDialog,QApplication,QPushButton,QHBoxLayout,
                             QVBoxLayout,QDesktopWidget,QTextBrowser,QLabel,
                             QLineEdit,QDateEdit,QMessageBox)
import qdarkstyle
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtSql import QSqlQuery,QSqlDatabase
from BOMDialog import BOMDialog
from MaterialDialog import MaterialDialog
from AllocateDialog import AllocateDialog
from StockDialog import StockDialog
from ComposeDialog import ComposeDialog
from ResultDialog import ResultDialog
from PyQt5.Qt import Qt
import math
import datetime

class MPSDialog(QDialog):
    def __init__(self):
        super(MPSDialog,self).__init__()
        self.setWindowModality (Qt.WindowModal)
        self.name = ""
        self.num = ""
        self.date = ""
        self.dic = []
        self.com = []
        self.initUI()
        self.displayTI()

    def initUI(self):
        self.resize(1000,600)
        self.setWindowTitle("myERP——MPS进度安排")
        self.setWindowIcon(QIcon("./image/Icon.png"))
        self.setStyleSheet (qdarkstyle.load_stylesheet_pyqt5 ())
        self.center()

        self.bombtn = QPushButton(self)
        self.bombtn.setText("BOM表")
        self.bombtn.setFont(QFont("苏新诗柳楷繁", 15))
        self.bombtn.setFixedSize(160, 40)
        self.bombtn.clicked.connect(self.bomdialog)

        self.mbtn = QPushButton(self)
        self.mbtn.setText("物料表")
        self.mbtn.setFont(QFont("苏新诗柳楷繁", 15))
        self.mbtn.setFixedSize(160, 40)
        self.mbtn.clicked.connect(self.materialdialog)

        self.abtn = QPushButton(self)
        self.abtn.setText("调配构成表")
        self.abtn.setFont(QFont("苏新诗柳楷繁", 15))
        self.abtn.setFixedSize(160, 40)
        self.abtn.clicked.connect(self.allocatedialog)

        self.sbtn = QPushButton(self)
        self.sbtn.setText("库存表")
        self.sbtn.setFont(QFont("苏新诗柳楷繁", 15))
        self.sbtn.setFixedSize(160, 40)
        self.sbtn.clicked.connect(self.stockdialog)

        self.cbtn = QPushButton(self)
        self.cbtn.setText("查看合成表")
        self.cbtn.setFont(QFont("苏新诗柳楷繁", 15))
        self.cbtn.setFixedSize(160, 40)
        self.cbtn.clicked.connect(self.composedialog)

        self.label1 = QLabel()
        self.label1.setText('当前MPS输入记录')
        self.label1.setFont(QFont("苏新诗柳楷繁", 15))

        self.label2 = QLabel()
        self.label2.setText('产品名称')
        self.label2.setFont(QFont("苏新诗柳楷繁", 12))
        self.te2 = QLineEdit()
        self.te2.setFont(QFont("苏新诗柳楷繁", 12))
        self.te2.setFixedSize(120,30)

        self.label3 = QLabel()
        self.label3.setText('数量')
        self.label3.setFont(QFont("苏新诗柳楷繁", 12))
        self.te3 = QLineEdit()
        self.te3.setFont(QFont("苏新诗柳楷繁", 12))
        self.te3.setFixedSize(120, 30)

        self.label4 = QLabel()
        self.label4.setText('完工日期')
        self.label4.setFont(QFont("苏新诗柳楷繁", 12))
        self.te4 = QDateEdit()
        self.te4.setFont(QFont("苏新诗柳楷繁", 12))
        self.te4.setFixedSize(120, 30)

        self.tb1 = QTextBrowser()
        self.tb1.setFixedSize(300,200)
        self.tb1.setFont(QFont("苏新诗柳楷繁", 12))

        self.addbtn = QPushButton(self)
        self.addbtn.setText("添加MPS记录")
        self.addbtn.setFont(QFont("苏新诗柳楷繁", 13))
        self.addbtn.setFixedSize(160, 30)
        self.addbtn.clicked.connect(self.addbtnClicked)

        self.clearbtn = QPushButton(self)
        self.clearbtn.setText("清空")
        self.clearbtn.setFont(QFont("苏新诗柳楷繁", 13))
        self.clearbtn.setFixedSize(100, 30)
        self.clearbtn.clicked.connect(self.clearbtnClicked)

        self.calbtn = QPushButton(self)
        self.calbtn.setText("计算")
        self.calbtn.setFont(QFont("苏新诗柳楷繁", 16))
        self.calbtn.setFixedSize(200,50)
        self.calbtn.clicked.connect(self.calbtnClicked)

        self.h1box = QHBoxLayout()
        self.h1box.addStretch(1)
        self.h1box.addWidget(self.bombtn)
        self.h1box.addStretch(1)
        self.h1box.addWidget(self.mbtn)
        self.h1box.addStretch(1)
        self.h1box.addWidget(self.abtn)
        self.h1box.addStretch(1)
        self.h1box.addWidget(self.sbtn)
        self.h1box.addStretch(1)

        self.h2box = QHBoxLayout()
        self.h2box.addStretch(1)
        self.h2box.addWidget(self.cbtn)
        self.h2box.addStretch(1)

        self.hsbox = QHBoxLayout()
        self.hsbox.addStretch(1)
        self.hsbox.addWidget(self.label2)
        self.hsbox.addWidget(self.te2)
        self.hsbox.addStretch(1)
        self.hsbox.addWidget(self.label3)
        self.hsbox.addWidget(self.te3)
        self.hsbox.addStretch(1)
        self.hsbox.addWidget(self.label4)
        self.hsbox.addWidget(self.te4)
        self.hsbox.addStretch(1)
        self.hsbox.addWidget(self.addbtn)
        self.hsbox.addStretch(1)
        self.hsbox.addWidget(self.clearbtn)
        self.hsbox.addStretch(1)

        self.hbbox = QHBoxLayout()
        self.hbbox.addWidget(self.calbtn)

        self.v31box = QVBoxLayout()
        self.v31box.addStretch(1)
        self.v31box.addWidget(self.label1)
        self.v31box.addStretch(1)
        self.v31box.addWidget(self.tb1)
        self.v31box.addStretch(1)

        self.v32box = QVBoxLayout()
        self.v32box.addStretch(1)
        self.v32box.addLayout(self.hbbox)
        self.v32box.addStretch(1)

        self.h3box = QHBoxLayout()
        self.h3box.addLayout(self.v31box)
        self.h3box.addLayout(self.v32box)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.h1box)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.h2box)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hsbox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.h3box)
        self.vbox.addStretch(1)
        self.setLayout(self.vbox)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def bomdialog(self):
        bomdialogWindow = BOMDialog()
        bomdialogWindow.show()
        bomdialogWindow.exec_()

    def materialdialog(self):
        materialdialogWindow = MaterialDialog()
        materialdialogWindow.show()
        materialdialogWindow.exec_()

    def allocatedialog(self):
        allocatedialogWindow = AllocateDialog()
        allocatedialogWindow.show()
        allocatedialogWindow.exec_()

    def stockdialog(self):
        stockdialogWindow = StockDialog()
        stockdialogWindow.show()
        stockdialogWindow.exec_()

    def composedialog(self):
        composedialogWindow = ComposeDialog()
        composedialogWindow.show()
        composedialogWindow.exec_()

    def addbtnClicked(self):
        self.name = self.te2.text()
        self.num = self.te3.text()
        self.date = self.te4.text()
        if(int(self.date.split('/')[1])<10):
            self.date = self.date[:5] + '0' + self.date[5:]
        if(int(self.date.split('/')[2])<10):
            self.date = self.date[:8] + '0' + self.date[8:]

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/myERP.db')
        db.open()
        query = QSqlQuery()
        if(self.name == "" or self.num == "" or self.date == ""):
            print(QMessageBox.warning(self, "警告", "你的表单有空白，请填写完整", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            sql = "select * from compose where childname = '%s'"%(self.name)
            query.exec_(sql)
            if not(query.next()):
                print(QMessageBox.warning(self, "警告", "您输入的物料并不在物料表中", QMessageBox.Yes, QMessageBox.Yes))
                return
            else:
                if(self.num.isnumeric() == False):
                    print(QMessageBox.warning(self, "警告", "您输入的数量并不合法", QMessageBox.Yes, QMessageBox.Yes))
                    return
                else:
                    sql = "insert into MPSinput values('%s',%d,'%s')" % (self.name,int(self.num),self.date.replace('/','-'))
                    query.exec_(sql)
                    db.commit()
                    db.close()
                    print(QMessageBox.information(self, "提示", "添加MPS记录成功", QMessageBox.Yes, QMessageBox.Yes))
                    self.te2.setText("")
                    self.te3.setText("")
                    self.displayTI()

    def clearbtnClicked(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/myERP.db')
        db.open()
        query = QSqlQuery()
        sql = "delete from MPSinput"
        query.exec_(sql)
        db.commit()
        db.close()
        self.displayTI()

    def displayTI(self):
        self.dic = []
        self.tb1.setText("")
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/myERP.db')
        db.open()
        query = QSqlQuery()
        sql = "select * from MPSinput"
        query.exec_(sql)
        while(query.next()):
            s = ""
            s = s + query.value(0) + " " + str(query.value(1)) + " " + query.value(2)
            self.dic.append([query.value(0),query.value(1),query.value(2)])
            self.tb1.append(s)
        db.commit()
        db.close()

    def calbtnClicked(self):
        self.com = []
        self.r = []
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/myERP.db')
        db.open()
        query = QSqlQuery()
        sql = "delete from MPSoutput"
        query.exec_(sql)
        sql = "select * from compose"
        query.exec_(sql)
        while(query.next()):
            self.com.append([query.value(0),query.value(1),query.value(2),
                             query.value(3),query.value(4),query.value(5),
                             query.value(6),query.value(7),query.value(8),
                             query.value(9),query.value(10)])
        for i in range(len(self.dic)):
            child = self.dic[i][0]
            num = self.dic[i][1]
            fdate = self.dic[i][2]
            s = []
            for j in range(len(self.com)):
                if(child == self.com[j][1]):
                    father = self.com[j][0]
            s.append(["","",child,float(num),"",fdate,father])
            while not(len(s) == 0):
                x = s.pop()
                for j in reversed(range(len(self.com))):
                    if(self.com[j][0] == x[6] and self.com[j][1] == x[2]):
                        x[0] = self.com[j][2]
                        x[1] = self.com[j][10]
                        if(x[3] / (1 - float(self.com[j][4])) > float(self.com[j][5]) + float(self.com[j][6])):
                            x[3] = x[3] / (1 - float(self.com[j][4])) \
                                   - float(self.com[j][5]) - float(self.com[j][6])
                            for k in range(len(self.com)):
                                if(self.com[k][1] == self.com[j][1]):
                                    self.com[k][5] = 0
                                    self.com[k][6] = 0
                        else:
                            if (x[3] / (1 - float(self.com[j][4])) <= float(self.com[j][5]) + float(self.com[j][6]) and x[3] / (1 - float(self.com[j][4])) > float(self.com[j][5])):
                                x = float(self.com[j][5]) + float(self.com[j][6]) - x[3] / (1 - float(self.com[j][4]))
                                for k in range(len(self.com)):
                                    if (self.com[k][1] == self.com[j][1]):
                                        self.com[k][5] = 0
                                        self.com[k][6] = x
                                x[3] = 0
                            else:
                                if (x[3] / (1 - float(self.com[j][4])) <= float(self.com[j][5])):
                                    x = float(self.com[j][5]) - x[3]
                                    if (self.com[k][1] == self.com[j][1]):
                                        self.com[k][5] = x
                                x[3] = 0
                        x[4] = (datetime.datetime.strptime(x[5],'%Y-%m-%d') - datetime.timedelta(days = int(self.com[j][7])) \
                               - datetime.timedelta(days = int(self.com[j][8])) - datetime.timedelta(days = int(self.com[j][9]))).strftime('%Y-%m-%d')
                self.r.append(x)
                for j in reversed(range(len(self.com))):
                    if(x[2] == self.com[j][0]):
                        s.append(["","",self.com[j][1],x[3] * int(self.com[j][3]),
                               "",x[4],self.com[j][0]])
        db.commit()
        db.close()
        self.uploadDatabase()
        self.resultDialog()

    def uploadDatabase(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/myERP.db')
        db.open()
        query = QSqlQuery()
        sql = "delete from MPSoutput"
        query.exec_(sql)
        for i in range(len(self.r)):
            sql = "insert into MPSoutput values('%s','%s','%s','%s','%s','%s')"\
                  %(self.r[i][0],self.r[i][1],self.r[i][2],str(math.ceil(self.r[i][3])),self.r[i][4],self.r[i][5])
            query.exec_(sql)
        db.commit()
        db.close()

    def resultDialog(self):
        resultdialogWindow = ResultDialog()
        resultdialogWindow.show()
        resultdialogWindow.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mpsWindow = MPSDialog()
    mpsWindow.show()
    sys.exit(app.exec_())