from . import invoker

@invoker
class binder:
    ''' '''
    def __getitem__(self,k):
        ''' '''
        return self.Second if k else self.First
    def __call__(self, func, **kw):
        ''' '''
        return func(**kw) 
    @classmethod
    def First(cls, func, arg,**kw):
        ''' '''
        def bind_first(get_arg):
            ''' '''
            return func(arg,get_arg,**kw)
        return bind_first
    @classmethod
    def Second(cls,func,arg,**kw):
        ''' '''
        def bind_second(get_arg):
            ''' '''
            return func(get_arg,arg,**kw)
        return bind_second
@invoker
class using:
    ''' '''
    def __call__(self, *a,**kw):
        ''' '''
        def using_func(func):
            ''' '''
            return func(*a,**kw)
        return using_func
    def Item(self,item):
        ''' '''
        def using_func_item(func):
            ''' '''
            return func(item)
        return using_func_item
    def Link(self,step,func):
        ''' '''
        return func(step)
