from PySide6.QtWidgets import  QApplication, QMainWindow,QVBoxLayout,QWidget,QPushButton,QToolBar,QStatusBar,QLineEdit,QLabel,QHBoxLayout
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
from PySide6.QtCore import QSize,Qt
from PySide6.QtGui import QAction,QIcon

 
class MainWindow(QMainWindow):

    def __init__( self):
        super().__init__()
        self.setWindowTitle("The Two Points Plotter")
        l = pg.mkPen(color=(255, 0, 0))
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground((211,211,211))   
        
        # plot data: x, y with initial zero values
        x = [0,0]
        y = [0,0]
        self.graphWidget.plot(x, y,l)        
      
    
       # plot button
        button=QPushButton("Press ME")
        button.clicked.connect(self.button_clikced)

        #setting slope,intercept labels 
        label=QLabel("Enter Slope ")
        self.line_edit=QLineEdit()
        self.line_2=QLineEdit()
        label2=QLabel("Enter Y intercept")       

        #layout for lines
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)
        h_layout.addWidget(label2)
        h_layout.addWidget(self.line_2)
        

        #widget layout
        layout = QVBoxLayout()
        layout.addLayout(h_layout)
        layout.addWidget(button)
        layout.addWidget(self.graphWidget)

        # Creat the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    # the slot
    def button_clikced(self,data):
            
            text1=self.line_edit.text()
            text2=self.line_2.text()
            x = float(text1) if text1 else 0
            y = float(text2) if text2 else 0
            xx = [0,100]
            yy=[xx[0]*x+y,xx[1]*x+y ]
            l = pg.mkPen(color=(255, 0, 0))
            self.graphWidget.plot(xx, yy,pen=l,symbol='+',symbolsize=30)
            self.graphWidget.setBackground('w')
            self.graphWidget.setLabel('left', 'Y-Axis')
            self.graphWidget.setLabel('bottom', 'X-Axis')
            
           
            
          

         
     