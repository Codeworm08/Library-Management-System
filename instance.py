import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
class Add_Instance(QDialog):
    def __init__(self):
        super(Add_Instance, self).__init__()
        uic.loadUi("AddInstance.ui",self)
        self.show()