from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from income import income_window

class saving_window(QWidget):
    def __init__(self):
        super().__init__()
       
        self.d= income_window()
        
        
        self.s_ui()

    def quit(self):
        self.close()
    def refreshed(self):

        #adding widgets to the daily page
        self.temp=income_window.temp_income
        self.tempt1=sum(self.temp["incomei"])
        self.tempt2=sum(self.temp["pocketi"])
        self.tempt3=sum(self.temp["gifti"])
        self.tempt4=sum(self.temp["otheri"])
        tt=self.tempt1+self.tempt2+self.tempt3+self.tempt4
        self.exp1.setText("Income is "+str(self.tempt1))
        self.exp2.setText("Allowance is "+str(self.tempt2))
        self.exp3.setText("Gift money is "+str(self.tempt3))
        self.exp4.setText("Other expenses are "+str(self.tempt4))
        self.texp.setText("Total income is "+str(tt))
        
        self.tempt1=sum(self.temp["travele"])
        self.tempt2=sum(self.temp["gifte"])
        self.tempt3=sum(self.temp["sociale"])
        self.tempt4=sum(self.temp["foode"])
        self.tempt5=sum(self.temp["housee"])
        tt=self.tempt1+self.tempt2+self.tempt3+self.tempt4
        self.inc1.setText("Travel is "+str(self.tempt1))
        self.inc2.setText("gift is "+str(self.tempt2))
        self.inc3.setText("Social  is "+str(self.tempt3))
        self.inc4.setText("Food  are "+str(self.tempt4))
        self.inc5.setText("House expenses are "+str(self.tempt5))
        self.tinc.setText("Total expense is "+str(tt))
    def s_ui(self):
        
        self.setWindowTitle("Savings")
        self.resize(400,400)
        self.goback=QPushButton("Go back")
       
        self.exp1=QLabel()  
        self.exp2=QLabel()
        self.exp3=QLabel()
        self.exp4=QLabel()
        self.texp=QLabel()
        layout=QVBoxLayout()
        layout2=QVBoxLayout()
        refresh=QPushButton("REFRESH")
        
        layout.addWidget(refresh)
       
        
        
        exited2=QPushButton("EXIT")
        
        self.inc1=QLabel()  
        self.inc2=QLabel()
        self.inc3=QLabel()
        self.inc4=QLabel()
        self.inc5=QLabel()
        self.tinc=QLabel()
        
        self.master_layout=QStackedLayout()
        
        layout2.addWidget(self.inc1)
        layout2.addWidget(self.inc2)
        layout2.addWidget(self.inc3)
        layout2.addWidget(self.inc4)
        layout2.addWidget(self.inc5)
        layout2.addWidget(self.tinc)
        layout2.addWidget(exited2)
        

        self.select_window=QMainWindow()
        self.select_window.resize(75,50)
        
        self.select_window.setWindowTitle("Select")
       
        select_layout=QVBoxLayout()
        select_layout.addWidget(QLabel("Select the day"))
        
        select_widget=QWidget()
        select_widget.setLayout(select_layout)
        self.select_window.setCentralWidget(select_widget)
        pg1=QWidget()
        pg2=QWidget()
        layout.addWidget(self.exp1)
        layout.addWidget(self.exp2)
        layout.addWidget(self.exp3)
        layout.addWidget(self.exp4)
        layout.addWidget(self.texp)
        
        self.daily_layout=QHBoxLayout()
        self.daily_layout.addLayout(layout)
        self.daily_layout.addLayout(layout2)
        
        pg1.setLayout(self.daily_layout)
        self.master_layout.addWidget(pg1)
        
        
        
        refresh.clicked.connect(self.refreshed)
        exited2.clicked.connect(self.quit)
       
       
        self.setLayout(self.master_layout)
    
        self.refreshed()