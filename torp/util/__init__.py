from ..import __cache__
from itertools import starmap as __it_star_map__

class invoker:
    ''' '''
    __cache__ = __cache__()
    def __new__(cls, target, *a, **kw):
        ''' '''
        return cls.__cache__.get(target, *a, **kw)
    @classmethod
    def With(cls, *a, **kw):
        ''' '''
        def invoke_with(target):
            ''' '''
            return cls(target, *a, **kw)
        return invoke_with

@invoker
class do:
    ''' '''
    @invoker
    class On:
        ''' '''
        def __call__(self, tup):
            ''' '''
            return self.PairFirst(tup)
        def PairFirst(self, tup):
            ''' '''
            return tup[0](tup[1])
        def PairSecond(self,tup):
            ''' '''
            return tup[1](tup[2])
    @invoker
    class For:
        ''' '''
        #TODO: flesh out
        def __call__(self, func, pairs):
            ''' '''
            return __it_star_map__(func,pairs)
    @invoker
    class Iter:
        #TODO: flesh out
        ''' '''
        def __call__(self, iterable):
            ''' '''
            for item in iterable: pass
