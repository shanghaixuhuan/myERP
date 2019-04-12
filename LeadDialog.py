import sys
from PyQt5.QtWidgets import (QDialog,QApplication,QVBoxLayout,QHBoxLayout,
                             QTextEdit,QLabel,QPushButton,QPlainTextEdit,QTextBrowser,
                             QFileDialog,QMessageBox)
import qdarkstyle
from PyQt5.QtGui import QIcon,QFont

class LeadDialog(QDialog):
    def __init__(self):
        super(LeadDialog,self).__init__()
        self.resize(800,600)
        self.setWindowTitle('myERP——导入购买记录')
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.init()

    def init(self):
        self.plabel = QLabel()
        self.plabel.setFont(QFont("苏新诗柳楷繁", 15))
        self.plabel.setText('请导入购买记录csv文件：')
        self.te = QTextEdit()
        self.te.setFixedSize(180,35)
        self.te.setFont(QFont("苏新诗柳楷繁", 13))
        self.sbutton = QPushButton()
        self.sbutton.setFixedSize(150,35)
        self.sbutton.setText('查询本地')
        self.sbutton.setFont(QFont("苏新诗柳楷繁", 13))
        self.sbutton.clicked.connect(self.inputFile)
        self.i1button = QPushButton()
        self.i1button.setFixedSize(120, 35)
        self.i1button.setText('导入')
        self.i1button.setFont(QFont("苏新诗柳楷繁", 13))
        self.i1button.clicked.connect(self.input1)
        self.alabel = QLabel()
        self.alabel.setFont(QFont("苏新诗柳楷繁", 15))
        self.alabel.setText('也可以手动输入购买记录：')
        self.pte = QPlainTextEdit()
        self.pte.setFixedSize(250,300)
        self.pte.setFont(QFont("苏新诗柳楷繁", 10))
        self.i2button = QPushButton()
        self.i2button.setFixedSize(120, 35)
        self.i2button.setText('导入')
        self.i2button.setFont(QFont("苏新诗柳楷繁", 13))
        self.i2button.clicked.connect(self.input2)
        self.rlabel = QLabel()
        self.rlabel.setFont(QFont("苏新诗柳楷繁", 15))
        self.rlabel.setText('当前输入结果为：')
        self.rtb = QTextBrowser()
        self.rtb.setFixedSize(250, 350)
        self.rtb.setFont(QFont("苏新诗柳楷繁", 10))
        self.cbutton = QPushButton()
        self.cbutton.setText('清空')
        self.cbutton.setFont(QFont("苏新诗柳楷繁", 13))
        self.cbutton.setFixedSize(120,35)
        self.cbutton.clicked.connect(self.clearText)

        self.h11box = QHBoxLayout()
        self.h11box.addWidget(self.te)
        self.h11box.addWidget(self.sbutton)
        self.h115box = QHBoxLayout()
        self.h115box.addStretch(1)
        self.h115box.addWidget(self.i1button)
        self.h115box.addStretch(1)
        self.h12box = QHBoxLayout()
        self.h12box.addStretch(1)
        self.h12box.addWidget(self.pte)
        self.h12box.addStretch(1)
        self.h125box = QHBoxLayout()
        self.h125box.addStretch(1)
        self.h125box.addWidget(self.i2button)
        self.h125box.addStretch(1)
        self.v1box = QVBoxLayout()
        self.v1box.addStretch(1)
        self.v1box.addWidget(self.plabel)
        self.v1box.addStretch(1)
        self.v1box.addLayout(self.h11box)
        self.v1box.addStretch(1)
        self.v1box.addLayout(self.h115box)
        self.v1box.addStretch(1)
        self.v1box.addWidget(self.alabel)
        self.v1box.addStretch(1)
        self.v1box.addLayout(self.h12box)
        self.v1box.addStretch(1)
        self.v1box.addLayout(self.h125box)
        self.v1box.addStretch(1)

        self.h21box = QHBoxLayout()
        self.h21box.addStretch(1)
        self.h21box.addWidget(self.cbutton)
        self.h21box.addStretch(1)
        self.v2box = QVBoxLayout()
        self.v2box.addStretch(1)
        self.v2box.addWidget(self.rlabel)
        self.v2box.addStretch(1)
        self.v2box.addWidget(self.rtb)
        self.v2box.addStretch(1)
        self.v2box.addLayout(self.h21box)
        self.v2box.addStretch(1)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.v1box)
        self.hbox.addStretch(1)
        self.hbox.addLayout(self.v2box)
        self.hbox.addStretch(1)

        self.setLayout(self.hbox)

        self.displayRecord()

    def displayRecord(self):
        f = open('./data/record.DAT','r')
        self.rtb.setText(f.read())
        f.close()

    def inputFile(self):
        self.filePath, fileType = QFileDialog.getOpenFileName(self, "选择购物记录", "", "*.csv;;All Files(*)")
        self.te.setText(self.filePath)

    def input1(self):
        if(self.te.toPlainText() == ""):
            print(QMessageBox.warning(self, "警告", "你没有选择任何文件！", QMessageBox.Yes, QMessageBox.Yes))
        else:
            try:
                f1 = open(self.te.toPlainText(),'r')
                f2 = open('./data/record.DAT','w')
                f2.write(f1.read())
                f1.close()
                f2.close()
                self.displayRecord()
                self.te.setText("")
                print(QMessageBox.information(self, "提示", "输入记录成功！", QMessageBox.Yes, QMessageBox.Yes))
            except Exception:
                print(QMessageBox.warning(self, "警告", "你选择的文件路径有错！", QMessageBox.Yes, QMessageBox.Yes))

    def input2(self):
        f = open('./data/record.DAT','w')
        f.write(self.pte.toPlainText())
        f.close()
        self.displayRecord()
        self.pte.setPlainText("")
        self.displayRecord()
        print(QMessageBox.information(self, "提示", "输入记录成功！", QMessageBox.Yes, QMessageBox.Yes))

    def clearText(self):
        f = open('./data/record.DAT','w')
        f.write("")
        f.close()
        self.displayRecord()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    leaddialogWindow = LeadDialog()
    leaddialogWindow.show()
    sys.exit(app.exec_())