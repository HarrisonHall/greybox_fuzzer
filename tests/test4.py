from .Test import Test
from .Conditional import Conditional

def test2_f(instrumentation, args):
    if Conditional("val1>250", lambda x : x[0] > 250, [0])(instrumentation, args):
        if Conditional("val1>251", lambda x : x[0] > 251, [0])(instrumentation, args):
            if Conditional("val2>251", lambda x : x[1] > 251, [1])(instrumentation, args):
                return
        if Conditional("val2>250", lambda x : x[1] > 250, [1])(instrumentation, args):
            return
        if Conditional("val2>150", lambda x : x[1] > 150, [1])(instrumentation, args):
            if Conditional("val2>200", lambda x : x[1] > 200, [1])(instrumentation, args):
                if Conditional("val2>202", lambda x : x[1] > 202, [1])(instrumentation, args):
                    return
    if Conditional("val1<10", lambda x : x[0] < 10, [0])(instrumentation, args):
        return
    if Conditional("val2>10", lambda x : x[1] > 10, [1])(instrumentation, args):
        if Conditional("val2>100", lambda x: x[1]>100, [1])(instrumentation, args):
            if Conditional("val2>200", lambda x : x[1] > 200, [1])(instrumentation, args):
                return
            if Conditional("val1>100", lambda x : x[0] > 100, [1])(instrumentation, args):
                if Conditional("val1<150", lambda x : x[0] < 150, [1])(instrumentation, args):
                    return
        if Conditional("val2>50", lambda x : x[1] > 50, [1])(instrumentation, args):
            if Conditional("val2>55", lambda x : x[1] > 50, [1])(instrumentation, args):
                return
    else:
        if Conditional("val1>=0;val2>=0", lambda x : True, [0, 1])(instrumentation, args):
            if Conditional("val1<=100;val2<=50", lambda x : x[0]<=100 and x[1]<=50, [0, 1])(instrumentation, args):
                return
        if Conditional("val1>=90;val2>=90", lambda x : x[0]>=90 and x[1]>=90, [0, 1])(instrumentation, args):
            if Conditional("val1<=110;val2<=110", lambda x : x[0]<=110 and x[1]<=110, [0, 1])(instrumentation, args):
                if Conditional("val1<=105;val2<=105", lambda x : x[0]<=105 and x[1]<=105, [0, 1])(instrumentation, args):
                    return
    
test4 = Test("test4", test2_f, 20, 2)
