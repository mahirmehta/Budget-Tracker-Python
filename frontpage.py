import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from expenses import expense_window
from income import income_window
from savings import saving_window

class MainWindow(QWidget):
    def __init__(self):
     super().__init__()
     
     self.w1=expense_window()
     self.w2=income_window()
     self.w3=saving_window()
     self.w3.close()
     self.ui()
    def show_window(self,w):
     self.w3.refreshed()
     w.show()

    def quit_main(self):
         self.w1.close()
         self.w2.close()
         #self.w3.close()
         self.close()

    def ui(self):
     self.setWindowTitle("Budget Tracker")
     self.resize(500,500)
     
     
     #adding widgets
     intro=QLabel("BUDGET TRACKER")
     button1=QPushButton("EXPENDITURE")
     button2= QPushButton("INCOME")
     button3=QPushButton("SAVINGS")
     button5=QPushButton("EXIT")

     button1.clicked.connect(lambda x:self.show_window(self.w1))
     button2.clicked.connect(lambda x:self.show_window(self.w2))
     button3.clicked.connect(lambda x:self.show_window(self.w3))
     button5.clicked.connect(self.quit_main)

     #setting widgets size
     intro.setMinimumSize(QSize(10,10))
     intro.setFont(QFont("Times New Roman",28))
     button1.setMinimumSize(QSize(125,75))
     button2.setMinimumSize(QSize(125,75))
     button3.setMinimumSize(QSize(125,75))
     button5.setMaximumSize(QSize(125,75))
     intro.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
     button1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
     button2.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
     button3.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)

     #adding widgets to layout
     layout=QVBoxLayout()
     layout1=QHBoxLayout()
     layout1.addWidget(intro)
     layout1.setSpacing(1)
     layout2=QHBoxLayout()
     layout3=QHBoxLayout()
     layout2.addWidget(button1)
     layout2.addWidget(button2)
     layout2.addWidget(button3)
     layout3.addWidget(button5)     
     layout.addLayout(layout1)
     layout.addLayout(layout2)
     layout.addLayout(layout3)
     
     self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    #app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
