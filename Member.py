import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
class AddMem(QDialog):
    def __init__(self):
        super(AddMem, self).__init__()
        uic.loadUi("AddMember.ui",self)
        self.show()