from .    import invoker
from copy import (deepcopy as __deep_copy__, copy as __copy__)

@invoker
class clone:
    ''' '''
    def __getitem__(self,k):
        ''' '''
        return __deep_copy__ if k else __copy__
    def __call__(self, obj, deep=False):
        ''' '''
        return self[deep](obj) 
    def Shallow(self,obj):
        ''' '''
        return self[0](obj)
    def Deep(self,obj):
        ''' '''
        return self[1](obj)
