from .Test import Test
from .Conditional import Conditional

def test1_f(instrumentation, args):
    if Conditional("val1>100", lambda x : x[0] > 100, [0])(instrumentation, args):
        if Conditional("val2>200", lambda x : x[1] > 200, [1])(instrumentation, args):
            return
    if Conditional("val1<50", lambda x : x[0] < 50, [0])(instrumentation, args):
        return
    
test1 = Test("test1", test1_f, 3, 2)


