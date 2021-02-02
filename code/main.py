#!/usr/bin/env python3

#
# file: main.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
from .program import MesonUi
import sys

def main_prog():
    app: MesonUi = MesonUi(sys_argv=sys.argv)
    app.boot()
    sys.exit(app.exec_())
