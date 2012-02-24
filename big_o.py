#!/usr/bin/env python
# -*- coding: utf-8 -*-



def find_max(x):
    """Find the maximum element in a list of positive integers."""
    max_ = 0
    for el in x:
        if el > max_:
            max_ = el
    return max_

import math
import time


print math.log(2, 3)
print math.log(2, 3*100)
now = time.time()
time.sleep(3)
print time.time() - now


#positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
#best, others = big_o.big_o(find_max, positive_int_generator, n_repeats=100)
#print others
