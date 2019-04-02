import sys
import qdarkstyle
from PyQt5.QtWidgets import (QWidget,QApplication,QLabel,QHBoxLayout,
                             QVBoxLayout,QPushButton)
from PyQt5.QtGui import QIcon,QPixmap,QFont
from PyQt5.QtCore import QCoreApplication
from AboutDialog import AboutDialog
from MPSDialog import MPSDialog

class HomePageWidget(QWidget):
    def __init__(self):
        super(HomePageWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,600)
        self.setWindowIcon(QIcon('./image/icon.png'))
        self.setWindowTitle('myERP——启动界面')

        self.titleLabel = QLabel(self)
        pixmap = QPixmap('./image/title.png')
        self.titleLabel.setPixmap(pixmap)
        self.htbox = QHBoxLayout()
        self.htbox.addStretch(1)
        self.htbox.addWidget(self.titleLabel)
        self.htbox.addStretch(1)

        self.mpsbtn = QPushButton(self)
        self.mpsbtn.setText("MPS进度安排")
        self.mpsbtn.setFont(QFont("苏新诗柳楷繁", 15))
        self.mpsbtn.clicked.connect(self.mpsdialog)
        self.mpsbtn.setFixedSize(160, 40)
        self.hmpsbox = QHBoxLayout()
        self.hmpsbox.addStretch(1)
        self.hmpsbox.addWidget(self.mpsbtn)
        self.hmpsbox.addStretch(1)

        self.abtn = QPushButton(self)
        self.abtn.setText("关    于")
        self.abtn.setFont(QFont("苏新诗柳楷繁", 15))
        self.abtn.clicked.connect(self.aboutdialog)
        self.abtn.setFixedSize(160, 40)
        self.habox = QHBoxLayout()
        self.habox.addStretch(1)
        self.habox.addWidget(self.abtn)
        self.habox.addStretch(1)

        self.qbtn = QPushButton(self)
        self.qbtn.setText("退    出")
        self.qbtn.setFont(QFont("苏新诗柳楷繁", 15))
        self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        self.qbtn.setFixedSize(160, 40)
        self.hqbox = QHBoxLayout()
        self.hqbox.addStretch(1)
        self.hqbox.addWidget(self.qbtn)
        self.hqbox.addStretch(1)


        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.htbox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hmpsbox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.habox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hqbox)
        self.vbox.addStretch(1)
        self.setLayout(self.vbox)

    def aboutdialog(self):
        aboutdialogWindow = AboutDialog()
        aboutdialogWindow.show()
        aboutdialogWindow.exec_()

    def mpsdialog(self):
        mpsdialogWindow = MPSDialog()
        mpsdialogWindow.show()
        mpsdialogWindow.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    HomePageWidget = HomePageWidget()
    HomePageWidget.show()
    sys.exit(app.exec_())