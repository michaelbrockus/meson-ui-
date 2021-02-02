#!/usr/bin/env python3

#
# file: base.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
from .subprojects import MesonSubprojects
from .configure import MesonConfigure
from .compile import MesonCompile
from .version import MesonVersion
from .test import MesonTest
from .init import MesonInit


class Command:

    def __init__(self) -> None:
        self.source_dir = None
        self.build_dir = None

        self.subprojects = MesonSubprojects()
        self.configure = MesonConfigure()
        self.compile = MesonCompile()
        self.version = MesonVersion()
        self.test = MesonTest()
        self.init = MesonInit()
