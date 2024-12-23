from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize


'''class Color(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette=self.palette()
        palette.setColor(QPalette.Window,QColor(color))'''


class MainWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Calculatrice")
        grid=QGridLayout()
        layout=QVBoxLayout()
        layout1=QVBoxLayout()
        layout2=QHBoxLayout()
        layout3=QHBoxLayout()

        self.setFixedSize(370,535)
        
        self.line=QLineEdit()
        self.line.setStyleSheet("background-color:#c0c0c0 ")
        f=QFont('Consolas',20)
        f1=QFont()
        f1.setPointSize(20)
        self.line.setFont(f) 
        self.line.setFixedSize(QSize(344,60))
        self.line.returnPressed.connect(self.a7sab)

        self.btn=QPushButton("CE")
        self.btn.setStyleSheet("background-color:#99CCFF")
        self.btn.pressed.connect(self.na7i)
        self.btn.setFont(f1) 
        self.btn.setFixedSize(QSize(80,80))
        layout3.addWidget(self.btn)
        self.btn=QPushButton("/")
        self.btn.setStyleSheet("background-color:#99CCFF")
        self.btn.pressed.connect(self.zidelha)
        self.btn.setFixedSize(QSize(80,80))
        self.btn.setFont(f1) 
        layout3.addWidget(self.btn)
        self.btn=QPushButton("*")
        self.btn.setStyleSheet("background-color:#99CCFF")
        self.btn.pressed.connect(self.zidelha)
        self.btn.setFixedSize(QSize(80,80))
        self.btn.setFont(f1)
        layout3.addWidget(self.btn)
        self.btn=QPushButton("C")
        self.btn.setStyleSheet("background-color:#99CCFF")
        self.btn.pressed.connect(self.na9es)
        self.btn.setFixedSize(QSize(80,80))
        self.btn.setFont(f1)
        layout3.addWidget(self.btn)
        self.btn=QPushButton("-")
        self.btn.setStyleSheet("background-color:#99CCFF")
        self.btn.pressed.connect(self.zidelha)
        self.btn.setFixedSize(QSize(80,80))
        self.btn.setFont(f1)
        layout1.addWidget(self.btn)
        self.btn=QPushButton("+")
        self.btn.setStyleSheet("background-color:#99CCFF")
        self.btn.pressed.connect(self.zidelha)
        self.btn.setFixedSize(QSize(80,80))
        self.btn.setFont(f1)
        layout1.addWidget(self.btn)
        self.btn=QPushButton("=")
        self.btn.setStyleSheet("background-color:#99CCFF")
        self.btn.pressed.connect(self.a7sab)
        self.btn.setFixedSize(QSize(80,169))
        self.btn.setFont(f1)
        layout1.addWidget(self.btn)
        
        l=["7","8","9","4","5","6","1","2","3","0","."]
        k=0
        for i in range(4):
            for j in range(3):
              if not (i==3 and j==0) :
                self.btn=QPushButton(l[k])
                self.btn.setStyleSheet("background-color:gray")
                self.btn.pressed.connect(self.zidelha)
                self.btn.setFixedSize(QSize(80,80))
                self.btn.setFont(f1)
                grid.addWidget(self.btn,i,j)
                k+=1

        layout2.addLayout(grid)
        layout2.addLayout(layout1)

        layout.addWidget(self.line)
        layout.addLayout(layout3)
        layout.addLayout(layout2)

        self.w=QWidget()
        self.w.setStyleSheet("background-color:black")
        self.w.setLayout(layout)

        self.setCentralWidget(self.w)
    
    def zidelha(self):
        b=self.sender()
        s=self.line.text()
        self.line.setText(s+b.text())

    def a7sab(self):
       try: 
        self.line.setText(str(eval(self.line.text())))
       except:
        self.line.setText("Erreur")
    
    def na9es(self):
       s=self.line.text()
       s=s[:len(s)-1]
       self.line.setText(s)

    def na7i(self):
       self.line.setText("")
        

app = QApplication([])

window = MainWindow()
window.show()

app.exec()