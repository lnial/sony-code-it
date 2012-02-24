#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_password(password):
    assert type(password) is str, "プログラマへ。パスワードが文字列じゃないってなにごと？"
    if len(password) < 4:
        raise Exception("パスワードが短すぎるよ！")
    else:
        return "OK!!!"



#print check_password([1, 2, 4])
print check_password("bf")
print check_password("aaaabf")



class Test(object):
    """test object"""
    def __init__(self):
        """__init__ documentation"""
        self._ff = 1
        self._fa = 1
    def ___get___(self):
        """method documentation"""
        return self._ff


if __name__ == '__main__':
    t = Test()
    #be able to access 
    print t.___get___()
    


