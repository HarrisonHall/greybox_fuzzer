class Test():
    """
    Testing object.
    """

    def __init__(self, name, function, branches, arguments):
        self.name = name
        self.function = function
        self.branches = branches
        self.arguments = arguments

    def __call__(self, instrumentation, vals):
        """
        Run the test given the value and instrumentation.
        """
        return self.function(instrumentation, vals)

    def visited_all_branches(self, instrumentation):
        """
        True if all branches have been visited.
        """
        return (
            len(instrumentation.conditional_to_count) == self.branches
        )

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self)
        
