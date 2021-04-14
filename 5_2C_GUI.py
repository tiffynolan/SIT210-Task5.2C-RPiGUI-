from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

blueLED = 16
greenLED = 20
redLED = 21

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Declare pin number standard
GPIO.setup(blueLED, GPIO.OUT) #Set pin mode
GPIO.setup(greenLED, GPIO.OUT) #Set pin mode
GPIO.setup(redLED, GPIO.OUT) #Set pin mode

class MyWindow(QMainWindow):
    #constructor
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 500, 300)
        self.setWindowTitle("Traffic Lights")
        self.initUI()

    def initUI(self):
        #label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Change Light Colour:")
        self.label.adjustSize() #auto adjust label size
        self.label.move(190, 10)

        #Blue Button
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Blue")
        self.b1.clicked.connect(self.BlueClicked)
        self.b1.move(200, 40)
        
        #Green Button
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Green")
        self.b2.clicked.connect(self.GreenClicked)
        self.b2.move(200, 80)
        
        #Red Button
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Red")
        self.b3.clicked.connect(self.RedClicked)
        self.b3.move(200, 120)
        
        #Off Button
        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Off")
        self.b4.clicked.connect(self.OffClicked)
        self.b4.move(200, 160)

    #Blue Light
    def BlueClicked(self):
        GPIO.output(blueLED, GPIO.HIGH)
        GPIO.output(greenLED, GPIO.LOW)
        GPIO.output(redLED, GPIO.LOW)
    
    #Green Light
    def GreenClicked(self):
        GPIO.output(blueLED, GPIO.LOW)
        GPIO.output(greenLED, GPIO.HIGH)
        GPIO.output(redLED, GPIO.LOW)
    
    #Red Light
    def RedClicked(self):
        GPIO.output(blueLED, GPIO.LOW)
        GPIO.output(greenLED, GPIO.LOW)
        GPIO.output(redLED, GPIO.HIGH)
        
    #Off
    def OffClicked(self):
        GPIO.output(blueLED, GPIO.LOW)
        GPIO.output(greenLED, GPIO.LOW)
        GPIO.output(redLED, GPIO.LOW) 


def window():
    #basic window setup
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show() #render
    sys.exit(app.exec_()) #exit
    
window()
