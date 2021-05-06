# import socket
# from usersock import ClientSock
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QFont
# construct clientSock class and bind ip and port with socket
# client = ClientSock(socket.gethostbyname(socket.gethostname()),5000)
# client.connect()

#initiallize GUI application
potatoApp = QApplication(sys.argv)
grid = QGridLayout()


#window and settings
potatoWindow = QWidget()
potatoWindow.setWindowTitle("Hey, potato is here!")
potatoWindow.setFixedSize(500,600)
potatoWindow.move(4000, 200)               #position of the window
potatoWindow.setStyleSheet("background: #FFFDD0;")

#display logo
helloPotato = QPixmap("hello.png")
welcomeImg = QLabel()
welcomeImg.setPixmap(helloPotato)
welcomeImg.setAlignment(QtCore.Qt.AlignCenter)
welcomeImg.setStyleSheet("margin-top: 200px;")

#add button
startButton = QPushButton("ask potato..")
startButton.setGeometry(200, 150, 100, 30)
startButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
startButton.setStyleSheet(
      "*{border: 2px solid '#E1865F';" +
      "border-radius: 13px;" +
      "background: '#E1865F';" +
      "font-size: 15px;" +
      "color: '#132733';" +
      "padding: 10px 0;" +
      "margin-top: 500px;" +
      "margin: 150px 150px;}" +
      "*:hover{background: '#D35A26';}" 
)
#add widgets to the grid
grid.addWidget(welcomeImg,0,0)
grid.addWidget(startButton, 0,0)

potatoWindow.setLayout(grid)
potatoWindow.show()
sys.exit(potatoApp.exec())
# while True:

#     msg = input("Enter msg to potato: ")

#     client.sendMsg(msg)
#     response = client.recvMsg()
#     print(response)