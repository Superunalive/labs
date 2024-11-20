#This Python file uses the following encoding: utf-8
import sys
import random as rand


def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield rand.randint(begin, end)
        i += 1

for i in gen_random(5, 4, 10):
    print(i, end=' ')