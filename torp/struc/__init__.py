from collections import ( Counter as __counter__, defaultdict as __default_dict__, deque as __deque__, namedtuple as __named_tuple__ )


class __cache__(dict):
    ''' '''
    def get(self, target, *a, **kw):
        ''' '''
        if target in self:
            return self[target]
        else:
            instance = self.__build__(target,*a,**kw)
            self[target] = instance
            return instance
    @classmethod
    def __build__(cls, target, *a, **kw):
        ''' '''
        return target(*a,**kw)

class container:
    ''' '''
    def __init__(self, **kw):
        self.__slots__ = tuple(kw.keys())
        for k,v in kw.items():
            setattr(self,k,v)
        has_call = self._has_call
        if has_call != -1:
            self.__doc__ = getattr(self[has_call],'__doc__',None)
    @property
    def _has_call(self):
        if '__call__' in self.__slots__:
            return self.__slots__.index('__call__')
        else:
            return -1
    def __call__(self,*a,**kw):
        if '__call__' in self.__slots__:
            x =  self.__slots__.index('__call__')
            return self[x](*a,**kw)
        else:
            pass
    def __iter__(self):
        yield from (getattr(self,n) for n in self.__slots__ )
    def __getitem__(self,k):
        if '__getitem__' in self.__slots__:
            print(k)
            return self.__slots__[self.__slots__.index('__getitem__')](k)
        elif isinstance(k,str):
            return getattr(self,k,None)
        elif isinstance(k,int) and k < len(self):
            return getattr(self, self.__slots__[k] ) 
    def __len__(self):
        return len(self.__slots__)
    def items(self):
        yield from ( (n,getattr(self,n)) for n in self.__slots__ )

class cache(__cache__):
    ''' '''
    @classmethod
    def __build__(cls, target, *a, **kw):
        ''' '''
        __methods__ = [(n,getattr(target,n)) for n in filter( str.isalpha, dir(target) ) ]
        if not hasattr(target,'__iter__'):
            setattr(target,'__iter__', classmethod(lambda cls : iter(cls.__methods__)) )
        setattr(target,'__methods__',__methods__)
        instance = target(*a,**kw)
        return instance

class cache_bound(cache):
    ''' '''
    def __init__(self, bound_pred, bound_wrap):
        self._bound_pred = bound_pred
        self._bound_wrap = bound_wrap
    def __filtered__(self,target):
        yield from ( (x,y) for x,y in vars(target).items() if self._bound_pred(y) )
    def __build__(self, target):
        items = { k : self._bound_wrap(v) for k,v in self.__filtered__(target) }
        return container(**items)

class cache_func(cache):
    ''' '''
    def __init__(self, func, use_args=False):
        self.func     = func
        self.use_args = use_args
    def __call__(self, arg, **kw):
        if not self.use_args:
            return self.func(arg, **kw)
        else:
            return self.func(*arg, **kw)
    def get(self, arg, **kw):
        if arg in self:
            return super().__getitem__(arg)
        else:
            cached = self(arg,**kw)
            self[arg] = cached
            return cached
    def __getitem__(self,arg):
        ''' '''
        return self.get(arg)
