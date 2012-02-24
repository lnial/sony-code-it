#!/usr/bin/env python
# -*- coding: utf-8 -*-

ONESTEP_TIME        = 2
OPEN_AND_CLOSE_TIME = 5

class Elevetor(object):
    """base matchine"""
    def __init__(self):
        """__init__ documentation"""
        self.time  = 0
        self.step  = 1
        self.human = 0
        self.line_index = []

        """input into self.line_index"""
        for line in file("input_i.csv"):
            list_temp  = []
            for i in line[:-1].rsplit(","):
                list_temp.append(int(i))
            self.line_index.append(list_temp)

    def _no_stop_move_(self, step_to):
        """elevetor がfromからtoまで動く

        >>> e = Elevetor()
        >>> e._no_stop_move(0, 3)
        6
        """
        self.time += abs(step_to - self.step) * ONESTEP_TIME
        self.time +=  OPEN_AND_CLOSE_TIME
        self.step = step_to

    def check_count(self):
        self.time += 1
        """elevetor have list people"""
        if self.line_index == []:
            print "fin"
            exit()
        for human_state in self.line_index:
            if human_state[1] <=  self.time:
                self._no_stop_move_(human_state[2])
                self._no_stop_move_(human_state[3])
                self.line_index = self.line_index[1:]
                print self.time
                return self.time
        return self.time


def _ex_test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    #_ex_test()
    el = Elevetor()
    times = 0

    while True:
        times = el.check_count()
        if times > 1000:
            exit()
    #line_index.sort(lambda x, y:x[2]-y[2])




    

