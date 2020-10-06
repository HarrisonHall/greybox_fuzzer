from .Test import Test

def test1_f(val, instrumentation):
    instrumentation("start", val)
    if val > 100:
        instrumentation("100", val)
        return
    if val < -100:
        instrumentation("-100", val)
        return
    instrumentation("end", val)
    
test1 = Test("test1", test1_f, 4)


