#This Python file uses the following encoding: utf-8
import sys

def print_result(function):
    print(function.__name__)
    def wrap(*args):
        a = function(*args)
        print(a)
        return a
    return wrap

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 2

@print_result
def test_3(num):
    return 3 + num

@print_result
def test_4():
    return 4

if __name__ == '__main__':
    
    test_1()
    test_2()
    test_3(10)
    test_4()
