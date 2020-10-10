from .Test import Test

def test2_f(val, instrumentation):
    instrumentation("start", val)
    if val > 100:
        instrumentation("100", val)
        if val > 101 and val < 105:
            instrumentation("100:2", val)
            if val == 104:
                instrumentaiton("104")
        return
    if val < -100:
        instrumentation("-100", val)
        if val * 2 == -500:
            instrumentation("-val*2==-500", val)
        return
    instrumentation("end", val)
    
deeptest1 = Test("deeptest1", test2_f, 7)


