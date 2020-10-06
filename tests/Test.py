class Test():
    """
    Testing object.
    """

    def __init__(self, name, function, branches):
        self.name = name
        self.function = function
        self.branches = branches

    def __call__(self, val, instrumentation):
        """
        Run the test given the value and instrumentation.
        """
        return self.function(val, instrumentation)

    def visited_all_branches(self, instrumentation):
        """
        True iff all branches have been visited.
        """
        return (
            len(instrumentation.position_to_values) == self.branches
        )

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self)
        
