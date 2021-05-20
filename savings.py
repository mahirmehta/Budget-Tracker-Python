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
        sav=tt
        self.exp1.setText("Income received is RS "+str(self.tempt1))
        self.exp2.setText("Allowance is Rs "+str(self.tempt2))
        self.exp3.setText("Gift money received is Rs "+str(self.tempt3))
        self.exp4.setText("Other icnome are Rs"+str(self.tempt4))
        self.texp.setText("Total income is "+str(tt))
        
        self.tempt1=sum(self.temp["travele"])
        self.tempt2=sum(self.temp["gifte"])
        self.tempt3=sum(self.temp["sociale"])
        self.tempt4=sum(self.temp["foode"])
        self.tempt5=sum(self.temp["housee"])
        self.tempt6=sum(self.temp["miscellaneouse"])
        tt=self.tempt1+self.tempt2+self.tempt3+self.tempt4+self.tempt5+self.tempt6
        sav=sav-tt
        self.inc1.setText("Travel expense is Rs "+str(self.tempt1))
        self.inc2.setText("Gifting expense is Rs "+str(self.tempt2))
        self.inc3.setText("Social expenses is Rs "+str(self.tempt3))
        self.inc4.setText("Food expenses are Rs "+str(self.tempt4))
        self.inc5.setText("House expenses are Rs "+str(self.tempt5))
        self.inc6.setText("Miscellaneous expenses are Rs "+str(self.tempt6))
        self.tinc.setText("Total expense is Rs "+str(tt))
        
        self.tsav.setText("Total savings are Rs "+str(sav))
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
        layout3=QHBoxLayout()
        refresh=QPushButton("REFRESH")
   
        exited2=QPushButton("EXIT")
        
        self.inc1=QLabel()  
        self.inc2=QLabel()
        self.inc3=QLabel()
        self.inc4=QLabel()
        self.inc5=QLabel()
        self.inc6=QLabel()
        self.tinc=QLabel()
        self.tsav=QLabel()
        
        layout2.addWidget(self.inc1)
        layout2.addWidget(self.inc2)
        layout2.addWidget(self.inc3)
        layout2.addWidget(self.inc4)
        layout2.addWidget(self.inc5)
        layout2.addWidget(self.inc6)
        layout2.addWidget(self.tinc)

        layout3.addWidget(refresh)
        layout3.addWidget(exited2)
   
        layout.addWidget(self.exp1)
        layout.addWidget(self.exp2)
        layout.addWidget(self.exp3)
        layout.addWidget(self.exp4)
        layout.addWidget(self.texp)
        
        self.daily_layout=QHBoxLayout()
        self.daily_layout.addLayout(layout)
        self.daily_layout.addLayout(layout2)

        main_layout=QVBoxLayout()
        main_layout.addLayout(self.daily_layout)
        main_layout.addWidget(self.tsav,0,Qt.AlignCenter)
        main_layout.addLayout(layout3)
     
        
        refresh.clicked.connect(self.refreshed)
        exited2.clicked.connect(self.quit)
       
        self.setLayout(main_layout)
    
        self.refreshed()
