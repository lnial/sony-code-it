#!/usr/bin/env python
# -*- coding: utf-8 -*-



K = 3


def reverse(one_a):
    """reverse"""
    if K < one_a:
        return one_a
    elif K == one_a:
        return True 
    else:
        one_a = one_a - K

def solve(one_a, two_b):
    """count reverse"""
    while reverse(one_a):
        print "one"

    print "finish"
if __name__ == '__main__':
    a = 5
    b = 3
    solve(a, b)
