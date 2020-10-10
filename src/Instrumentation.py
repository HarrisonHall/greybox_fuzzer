class Instrumentation:
    """
    Provide instrumentation to test like a greybox fuzzer would.
    """
    
    NEW_POSITION, OLD_POSITION = range(2)
    
    def __init__(self):
        self.conditional_to_values = {}
        self.value_to_condionals = {}
        self.conditional_to_count = {}
        self.current_run = []
        self.current_failures = []

    def __call__(self, position, triggered_value):
        """
        Record instrumentation.
        """
        if position not in self.position_to_values:
            self.position_to_values[position] = set()
        self.position_to_values[position].add(triggered_value)
            
        if triggered_value in self.value_to_positions:
            self.value_to_positions[triggered_value].add(position)
            return self.NEW_POSITION
        else:
            self.value_to_positions[triggered_value] = set([position])
            return self.OLD_POSITION

    def add_success(self, args, conditional):
        self.current_run.append(conditional)
        targs = tuple(args)
        """
        if targs in self.value_to_condionals:
            self.value_to_condionals[targs].append(conditional)
        else:
            self.value_to_condionals[targs] = [conditional]
        """
        """
        if conditional in self.conditional_to_values:
            self.conditional_to_values[conditional].append(targs)
        else:
            self.conditional_to_values[conditional] = [targs]
        self.conditional_to_count[conditional] = self.conditional_to_count.get(conditional, 0) + 1
        """
        

    def add_failure(self, args, conditional):
        self.current_failures.append(conditional)

    def reset_run(self):
        self.current_run = []
        self.current_failure = None

    def num_branches(self):
        """
        Returns the number of unique branches visited.
        """
        return len(self.position_to_values)
