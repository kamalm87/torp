from .         import invoker
from functools import partial as __ft_part__, reduce as __ft_reduce__, update_wrapper as __ft_update_wrapper__

@invoker
class piper:
    @staticmethod
    def Link(item,func):
        ''' '''
        return func(item)
    @staticmethod
    def Swallow(*a,**kw):
        ''' '''
        return a, kw
    @staticmethod
    def Wrap(func):
        ''' '''
        def head_func(*a,**kw):
            ''' '''
            return func(*a,**kw)
        return head_func
    @classmethod
    def Head(cls, funcs):
        ''' '''
        wrapped = cls.Wrap( funcs[0] if len(funcs) else self.Swallow )
        return wrapped
    @classmethod
    def Create(cls,funcs):
        ''' '''
        funcs = tuple(funcs)
        head  = cls.Head(funcs)
        pipes = __ft_part__( __ft_reduce__, cls.Link, funcs[1:])
        def pipe_function(*a,**kw):
            ''' '''
            return pipes(head(*a,**kw))
        return __ft_update_wrapper__(pipe_function,funcs[0])
    def __call__(self, *funcs):
        return self.Create( tuple(__YIELD__(*funcs)))
