#!/usr/bin/env python3

#
# file: view_main.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from ..viewable.main import Ui_ActivityMain

class ViewMain(QMainWindow, Ui_ActivityMain):
    def __init__(self) -> None:
        super(self.__class__, self).__init__()
        self.setupUi(self)
