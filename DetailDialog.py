import sys
from PyQt5.QtWidgets import (QDialog,QLabel,QApplication,QVBoxLayout,
                             QHBoxLayout,QTextBrowser)
import qdarkstyle
from PyQt5.QtGui import QIcon,QPixmap,QFont
from PyQt5.QtSql import QSqlQuery,QSqlDatabase


class GoodDetailDialog(QDialog):
    def __init__(self,GoodId):
        super(GoodDetailDialog,self).__init__()
        self.str = GoodId
        self.resize(800,600)
        self.setWindowTitle("myERP——商品详情")
        self.setWindowIcon(QIcon("./image/icon.png"))
        self.initUI()

    def initUI(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('./db/myERP.db')
        self.db.open()
        self.query = QSqlQuery()
        sql = "select * from goods where id = '%s'" %(self.str)
        self.query.exec_(sql)
        self.query.next()

        id = self.query.value(0)
        name = self.query.value(1)
        company = self.query.value(2)
        date = self.query.value(3)
        price = self.query.value(4)
        img = self.query.value(5)
        screen = self.query.value(6)
        CPU = self.query.value(7)
        GPU = self.query.value(8)
        advantage = self.query.value(9)
        disadvantage = self.query.value(10)

        self.labeltitle = QLabel(self)
        self.imagetitle = QPixmap()
        self.imagetitle.load(img)
        self.labeltitle.setFixedSize(350,250)
        self.labeltitle.setPixmap(self.imagetitle.scaled(self.labeltitle.width(), self.labeltitle.height()))
        self.h1box = QHBoxLayout()
        self.h1box.addStretch(1)
        self.h1box.addWidget(self.labeltitle)
        self.h1box.addStretch(1)

        self.idlabel = QLabel()
        self.idlabel.setText('商品编号：')
        self.idlabel.setFont(QFont("苏新诗柳楷繁", 13))
        self.idlabel_ = QLabel()
        self.idlabel_.setFont(QFont("苏新诗柳楷繁", 13))
        self.idlabel_.setText(id)
        self.pricelabel = QLabel()
        self.pricelabel.setText('商品价格：')
        self.pricelabel.setFont(QFont("苏新诗柳楷繁", 13))
        self.pricelabel_ = QLabel()
        self.pricelabel_.setFont(QFont("苏新诗柳楷繁", 13))
        self.pricelabel_.setText(str(price))
        self.h2box = QHBoxLayout()
        self.h2box.addStretch(1)
        self.h2box.addWidget(self.idlabel)
        self.h2box.addWidget(self.idlabel_)
        self.h2box.addStretch(1)
        self.h2box.addWidget(self.pricelabel)
        self.h2box.addWidget(self.pricelabel_)
        self.h2box.addStretch(1)

        self.namelabel = QLabel()
        self.namelabel.setText('商品名称：')
        self.namelabel.setFont(QFont("苏新诗柳楷繁", 13))
        self.namelabel_ = QLabel()
        self.namelabel_.setFont(QFont("苏新诗柳楷繁", 13))
        self.namelabel_.setText(name)
        self.h3box = QHBoxLayout()
        self.h3box.addStretch(1)
        self.h3box.addWidget(self.namelabel)
        self.h3box.addWidget(self.namelabel_)
        self.h3box.addStretch(1)

        self.companylabel = QLabel()
        self.companylabel.setText('上市日期：')
        self.companylabel.setFont(QFont("苏新诗柳楷繁", 13))
        self.companylabel_ = QLabel()
        self.companylabel_.setFont(QFont("苏新诗柳楷繁", 13))
        self.companylabel_.setText(date)
        self.h4box = QHBoxLayout()
        self.h4box.addStretch(1)
        self.h4box.addWidget(self.companylabel)
        self.h4box.addWidget(self.companylabel_)
        self.h4box.addStretch(1)

        self.screenlabel = QLabel()
        self.screenlabel.setText('屏幕：')
        self.screenlabel.setFont(QFont("苏新诗柳楷繁", 13))
        self.screenlabel_ = QLabel()
        self.screenlabel_.setFont(QFont("苏新诗柳楷繁", 13))
        self.screenlabel_.setText(screen)
        self.CPUlabel = QLabel()
        self.CPUlabel.setText('CPU：')
        self.CPUlabel.setFont(QFont("苏新诗柳楷繁", 13))
        self.CPUlabel_ = QLabel()
        self.CPUlabel_.setFont(QFont("苏新诗柳楷繁", 13))
        self.CPUlabel_.setText(CPU)
        self.h5box = QHBoxLayout()
        self.h5box.addStretch(1)
        self.h5box.addWidget(self.screenlabel)
        self.h5box.addWidget(self.screenlabel_)
        self.h5box.addStretch(1)
        self.h5box.addWidget(self.CPUlabel)
        self.h5box.addWidget(self.CPUlabel_)
        self.h5box.addStretch(1)

        self.GPUlabel = QLabel()
        self.GPUlabel.setText('GPU：')
        self.GPUlabel.setFont(QFont("苏新诗柳楷繁", 13))
        self.GPUlabel_ = QLabel()
        self.GPUlabel_.setFont(QFont("苏新诗柳楷繁", 13))
        self.GPUlabel_.setText(GPU)
        self.h6box = QHBoxLayout()
        self.h6box.addStretch(1)
        self.h6box.addWidget(self.GPUlabel)
        self.h6box.addWidget(self.GPUlabel_)
        self.h6box.addStretch(1)

        self.adlabel = QLabel()
        self.adlabel.setText('优点：')
        self.adlabel.setFont(QFont("苏新诗柳楷繁", 13))
        self.adtb = QTextBrowser()
        self.adtb.setText(advantage)
        self.adtb.setFixedSize(250,200)
        self.adtb.setFont(QFont("苏新诗柳楷繁", 12))
        self.disadtb = QTextBrowser()
        self.disadtb.setText(disadvantage)
        self.disadtb.setFixedSize(250,200)
        self.disadtb.setFont(QFont("苏新诗柳楷繁", 12))
        self.disadlabel = QLabel()
        self.disadlabel.setText('缺点：')
        self.disadlabel.setFont(QFont("苏新诗柳楷繁", 13))

        self.v1box = QVBoxLayout()
        self.v1box.addLayout(self.h1box)
        self.v1box.addLayout(self.h2box)
        self.v1box.addLayout(self.h3box)
        self.v1box.addLayout(self.h4box)
        self.v1box.addLayout(self.h5box)
        self.v1box.addLayout(self.h6box)

        self.v2box = QVBoxLayout()
        self.v2box.addStretch(1)
        self.v2box.addWidget(self.adlabel)
        self.v2box.addWidget(self.adtb)
        self.v2box.addStretch(1)
        self.v2box.addWidget(self.disadlabel)
        self.v2box.addWidget(self.disadtb)
        self.v2box.addStretch(1)


        self.htbox = QHBoxLayout()
        self.htbox.addStretch(1)
        self.htbox.addLayout(self.v1box)
        self.htbox.addStretch(1)
        self.htbox.addLayout(self.v2box)
        self.htbox.addStretch(1)

        self.recolabel = QLabel()
        self.recolabel.setText('您可能还对以下商品感兴趣：')
        self.recolabel.setFont(QFont("苏新诗柳楷繁", 12))

        self.hbbox = QHBoxLayout()

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.htbox)
        self.vbox.addWidget(self.recolabel)
        self.vbox.addLayout(self.hbbox)

        self.setLayout(self.vbox)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    gooddetaildialogWindow = GoodDetailDialog("01")
    gooddetaildialogWindow.show()
    sys.exit(app.exec_())