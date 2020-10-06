class Instrumentation:
    """
    Provide intstrumentation to tests like a greybox fuzzer would.
    """
    
    NEW_POSITION, OLD_POSITION = range(2)
    
    def __init__(self):
        self.position_to_values = {}
        self.value_to_positions = {}

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

    def num_branches(self):
        """
        Returns the number of unique branches visited.
        """
        return len(self.position_to_values)
