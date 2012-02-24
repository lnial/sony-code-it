#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

 
def solve1(_input, _sum):
   if _input == 0:
       return _sum
   else:
       _sum = _input * _sum
       return solve1(_input - 1, _sum)

def solve2(_input, _sum):
    return math.gamma(_input + 1)


#if __name__ == '__main__':
#    factorial_real = [1.1, 2.5, 3.3, 4.4, 5.5]
#    sum_store = 1
#    for i in factorial_real:
#        print solve2(i, sum_store)
#    #for i in range(1, 14):
#    #    print solve1(i, sum_store)

class Test(object):
    """class documentation"""
    def __init__(self):
        """__init__ documentation"""
        self._x = 1

    def aaa(self, a):
        """
        documentation
        >>> t = Test()
        >>> t.aaa(1)
        'OK'
        """
        return "OK"

    def bbb(self, b):
        """bbb"""
        """
        bbb test
        >>> t = Test()
        >>> t.bbb(2)
        'No'
        """
        return "NO"


def _ex_test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    #t = Test()
    #print t.__class__.__name__
    _ex_test()




    
