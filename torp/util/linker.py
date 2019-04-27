from .         import invoker
from itertools import chain as __it_chain__

@invoker
class linker:
    ''' '''
    def __call__(self, *items, iterable=False):
        ''' '''
        return self[iterable](items)
    def __getitem__(self,k):
        ''' '''
        return __it_chain__.from_iterable if k else __it_chain__
    def Items(self,*items):
        ''' '''
        return self[0](items)
    def Iterables(self,*iterables):
        ''' '''
        return self[1](iterables)
