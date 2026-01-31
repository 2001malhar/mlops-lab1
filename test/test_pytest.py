import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import fun1, fun2, fun3

def test_fun1():
    assert fun1(2, 3) == 5
    assert fun1(-1, 1) == 0
    assert fun1(0, 0) == 0

def test_fun2():
    assert fun2(5, 3) == 2
    assert fun2(10, 5) == 5
    assert fun2(0, 0) == 0

def test_fun3():
    assert fun3(2, 3) == 6
    assert fun3(5, 4) == 20
    assert fun3(0, 10) == 0
