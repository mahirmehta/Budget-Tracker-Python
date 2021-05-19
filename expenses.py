import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from income import income_window

class expense_window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.money=QTextEdit("")
        self.money1=QTextEdit("")
        self.money2=QTextEdit("")
        self.money3=QTextEdit("")
        self.money4=QTextEdit("")
        self.money5=QTextEdit("")
        self.money6=QTextEdit("")
        self.l=[self.money,self.money1,self.money2,self.money3,self.money4,self.money6,self.money5]
        self.ti=income_window()
        self.l2=[]
        self.e_ui()
    def save(self):
        temp_income=income_window.temp_income
        for x in self.l:
            i=0                               
            temp1=x.toPlainText()
            temp1.replace(" ","")
            if temp1 != "":
                try:
                    i=int(temp1)
                except:
                    x.setText("Error")
         
            self.l2.append(i)
        temp_income["travele"].append(self.l2[0])
        temp_income["sociale"].append(self.l2[1])
        temp_income["gifte"].append(self.l2[2])
        temp_income["foode"].append(self.l2[3])
        temp_income["housee"].append(self.l2[4])
        temp_income["sociale"].append(self.l2[5])
        temp_income["miscellaneouse"].append(self.l2[6])
        self.l2.clear()
        self.money.setText("")
        self.money1.setText("")
        self.money2.setText("")
        self.money3.setText("")
        self.money4.setText("")
        self.money6.setText("")
        self.money5.setText("")
        
    def exit_deposit(self):
        self.money.setText("")
        self.money1.setText("")
        self.money2.setText("")
        self.money3.setText("")
        self.money4.setText("")
        self.money5.setText("")
        self.money6.setText("")
        self.close()   
    def e_ui(self): 
      self.setWindowTitle("Expesnes")
      self.resize(400,400)
      saved=QPushButton("Save")
      travel=QRadioButton("Travel")
      gift=QRadioButton("Gift")
      social=QRadioButton("Social Meeting")
      food=QRadioButton("Food")
      house=QRadioButton("Household expenses")
      miscellaneous=QRadioButton("Miscellaneous")
      quit_deposit=QPushButton("EXIT")
      self.money.setMaximumSize(QSize(75,23))
      self.money1.setMaximumSize(QSize(75,23))
      self.money2.setMaximumSize(QSize(75,23))
      self.money3.setMaximumSize(QSize(75,23))
      self.money4.setMaximumSize(QSize(75,23))
      self.money5.setMaximumSize(QSize(75,23))
      self.money6.setMaximumSize(QSize(75,23))
      quit_deposit.setMaximumSize(QSize(100,50))
      quit_deposit.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
      

      layout=QVBoxLayout()
      line1=QHBoxLayout()
      line2=QHBoxLayout()
      line3=QHBoxLayout()
      line4=QHBoxLayout()
      line5=QHBoxLayout()
      line6=QHBoxLayout()
      line_exit=QHBoxLayout()

      line1.addWidget(travel,1,Qt.AlignLeft)
      line1.addWidget(self.money)
      line2.addWidget(gift,1,Qt.AlignLeft)
      line2.addWidget(self.money2)
      line3.addWidget(food,1,Qt.AlignLeft)
      line3.addWidget(self.money3)
      line4.addWidget(house,1,Qt.AlignLeft)
      line4.addWidget(self.money4)
      line5.addWidget(social,1,Qt.AlignLeft)
      line5.addWidget(self.money6)
      line6.addWidget(miscellaneous,1,Qt.AlignLeft)
      line6.addWidget(self.money5)
      line_exit.addWidget(quit_deposit,1,Qt.AlignCenter)
      
      

      layout.addLayout(line1)
      layout.addLayout(line2)
      layout.addLayout(line3)
      layout.addLayout(line4)
      layout.addLayout(line5)
      layout.addLayout(line6)
      layout.addLayout(line_exit)
      layout.addWidget(saved,0,Qt.AlignCenter)
   
    
      

      self.setLayout(layout)
      
      saved.clicked.connect(self.save)
      quit_deposit.clicked.connect(self.exit_deposit)
