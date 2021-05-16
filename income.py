import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class income_window(QWidget):
    temp_income = {"incomei":[0],"pocketi":[0],"gifti":[0],"otheri":[0],"travele":[0],"gifte":[0],"sociale":[0],"foode":[0],"housee":[0]}
    def __init__(self):
        super().__init__()
        self.t1=QTextEdit("")
        self.t2=QTextEdit("")
        self.t3=QTextEdit("")
        self.t4=QTextEdit("")
        self.l=[self.t1,self.t2,self.t3,self.t4]
        
        
        self.l2=[]
        self.i_ui()
        
        

    def quit_income(self):
        self.t1.setText("")
        self.t2.setText("")
        self.t3.setText("")
        self.t4.setText("")
        self.close()

    def save_income(self):
        for x in range(0,4):
            i=0                               
            temp1=self.l[x].toPlainText()
            temp1.replace(" ","")
            if temp1 != "":
                try:
                    i=int(temp1)
                except:
                    self.l[x].setText("Error")
         
            self.l2.append(i)
        self.temp_income["incomei"].append(self.l2[0])
        self.temp_income["pocketi"].append(self.l2[1])
        self.temp_income["gifti"].append(self.l2[2])
        self.temp_income["otheri"].append(self.l2[3])
        self.l2.clear()
        self.t1.setText("")
        self.t2.setText("")
        self.t3.setText("")
        self.t4.setText("")

    def i_ui(self):
        self.setWindowTitle("Income")
        self.resize(400,400)
        label1=QLabel("Income")
        label2=QLabel("Pocket Money")
        label3=QLabel("Gifts")
        label4=QLabel("Other")
        add=QPushButton("Save")
        exit_deposit=QPushButton("Exit")
              
        self.t1.setMaximumSize(QSize(80,24))
        self.t2.setMaximumSize(QSize(80,24))
        self.t3.setMaximumSize(QSize(80,24))
        self.t4.setMaximumSize(QSize(80,24))

        layout=QVBoxLayout()
        l1=QHBoxLayout()
        l2=QHBoxLayout()
        l3=QHBoxLayout()
        l4=QHBoxLayout()
        l1.addWidget(label1,1,Qt.AlignLeft)
        l1.addWidget(self.t1,0,Qt.AlignCenter)
        l2.addWidget(label2,1,Qt.AlignLeft)
        l2.addWidget(self.t2,0,Qt.AlignCenter)
        l3.addWidget(label3,1,Qt.AlignLeft)
        l3.addWidget(self.t3,0,Qt.AlignCenter)
        l4.addWidget(label4,1,Qt.AlignLeft)
        l4.addWidget(self.t4,0,Qt.AlignCenter)
        layout.addLayout(l1)
        layout.addLayout(l2)
        layout.addLayout(l3)
        layout.addLayout(l4)
        layout.addWidget(add,0,Qt.AlignCenter)
        layout.addWidget(exit_deposit,0,Qt.AlignCenter)
        
        self.setLayout(layout)

        exit_deposit.clicked.connect(self.quit_income)
        add.clicked.connect(self.save_income)