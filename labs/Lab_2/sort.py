#This Python file uses the following encoding: utf-8
import sys
import math

data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = sorted(data, key = abs, reverse = True)
    print(result)
    
    result_with_lambda = sorted(data, key = lambda k: abs(k), reverse = True)
    print(result_with_lambda)