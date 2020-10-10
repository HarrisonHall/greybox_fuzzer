class Conditional:
    """
    Wrapper class for statement conditionals inside tests.
    """
    
    def __init__(self, name, function, args):
        self.function = function  # function pointer to execute
        self.args = args  # list of argument positions
        self.name = name  # string name

    def evaluate(self, *args):
        return self.function(*args)

    def arg_count(self):
        assert self.function.__code__.co_argcount == len(self.args)
        return self.function.__code__.co_argcount

    def __eq__(self, other):
        if isinstance(other, Conditional):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        return False

    def __bool__(self):
        return bool(self.evaluate())

    def __call__(self, instrumentation, *args):
        #self.args = args
        if isinstance(args, tuple):
            args = args[0]
        success = self.function(args)
        if success:
            instrumentation.add_success(args, self)
        else:
            instrumentation.add_failure(args, self)
        return success

    def __hash__(self):
        return hash(self.name)
