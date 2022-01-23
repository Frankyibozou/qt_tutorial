import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QHBoxLayout,QWidget,QPushButton
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self, ):
        super(FirstMainWin, self).__init__()
        self.setWindowTitle('close the window')
        self.resize(400, 300)
        # add a pushbuttion
        self.button1=QPushButton('close the applicaiton')
        self.button1.clicked.connect(self.onClick_Button)

        layout=QHBoxLayout()
        layout.addWidget(self.button1)


        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    # click method

    def onClick_Button(self):
        sender=self.sender()
        print(sender.text()+'is pushed')
        app=QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
