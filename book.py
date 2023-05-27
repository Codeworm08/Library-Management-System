import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
class Add_B(QDialog):
    def __init__(self):
        super(Add_B, self).__init__()
        uic.loadUi("AddBook.ui",self)
        self.show()