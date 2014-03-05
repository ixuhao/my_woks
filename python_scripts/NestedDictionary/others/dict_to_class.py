# -*- coding: utf-8 -*-
# http://www.blog.pythonlibrary.org/2014/02/14/python-101-how-to-change-a-dict-into-a-class/

class Dict2Obj(object):
    """
    Turns a dictionary into a class
    """
    def __init__(self, dictionary):
        """ Constructor """
        for key in dictionary:
            setattr(self, key, dictionary[key])
    def __repr__(self):
        """"""
        #attrs = str([x for x in self.__dict__])
        attrs = str([x for x in dir(self) if '__' not in x])
        return "<Dict2Obj>: %s" % attrs

class DictToObj(object):
    """
    Turns dictionary to class
    """
    def __init__(self, dictionary, merge=lambda s, k, v: setattr(s, k, v)):
        for k, v in dictionary.iteritems():
            merge(self, k, v)

    def __repr__(self):
        """"""
        attrs = str([x for x in dir(self) if '__' not in x])
        return "<DictToObj>: %s" % attrs

def Upper(s):
    return s.upper()

if __name__ == '__main__':
    ball_dict = {"color":"blue",
                 "size":"8 inches",
                 "material":"rubber"}
    ball = Dict2Obj(ball_dict)
    ball.color = 'red'
    ball.key = 'my key'
    for k in ball.__dict__:
        if 'k' in k:
            setattr(ball, k, lambda s: s.upper())
            print getattr(ball, k)

    # if really just want to quickly convert dict to object
    dc = type('D', (object,), ball_dict)()
    print dc.color
    dc.size = '12 inches'
    dc.man = 'mine'
    print dc.__dict__
    print dir(dc)

    # try DictToObj
    bdh = DictToObj(ball_dict)
    bdh.material = 'glass'
    bdh.key = 'yellow'
    print bdh.material
    print bdh.__dict__
