#!/usr/bin/env python3

#
# file: run_tests.py
# author: Michael Brockus
# gmail: <michaelbrockus@gmail.com>
#
from code.program import greet


def test_basic_assert_works():
    assert True

def test_greet_not_none():
    assert greet() is not None
