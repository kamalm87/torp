from .               import invoker
from collections.abc import Iterable as __abc_iterable__

@invoker
class yielder:
    ''' '''
    @staticmethod
    def _is_yieldable(item):
        ''' '''
        return isinstance(item,__abc_iterable__) and not isinstance(item,str)
    def __call__(self, *items):
        ''' '''
        for item in items:
            (yield from self(*item)) if self._is_yieldable(item) else (yield item)

@invoker
class consumer:
    ''' '''
    def __call__(self, iterable):
        ''' '''
        for item in iterable: pass
    def Items(self,*items):
        ''' '''
        self(items)
