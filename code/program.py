#!/usr/bin/env python3

#
# file: program.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
from PyQt5.QtWidgets import QApplication


class MesonUi(QApplication):
    def __init__(self, sys_argv):
        super(self.__class__, self).__init__(sys_argv)

    def boot(self):
        self.activity = None


def greet():
    return "Hello, Python Developer"
