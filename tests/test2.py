from .Test import Test
from .Conditional import Conditional

def test2_f(instrumentation, args):
    if Conditional("val1>250", lambda x : x[0] > 250, [0])(instrumentation, args):
        if Conditional("val1>251", lambda x : x[0] > 251, [0])(instrumentation, args):
            pass
        if Conditional("val2>250", lambda x : x[1] > 250, [1])(instrumentation, args):
            return
    if Conditional("val1<10", lambda x : x[0] < 10, [0])(instrumentation, args):
        return
    if Conditional("val2>10", lambda x : x[1] > 10, [1])(instrumentation, args):
        if Conditional("val2>100", lambda x: x[1]>100, [1])(instrumentation, args):
            if Conditional("val2>200", lambda x : x[1] > 200, [1])(instrumentation, args):
                return
    else:
        if Conditional("val1>=0;val2>=0", lambda x : True, [0, 1])(instrumentation, args):
            pass
    
test2 = Test("test2", test2_f, 9, 2)
