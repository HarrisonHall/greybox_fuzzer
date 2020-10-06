class Matryoshka:
    """
    Our implementation of matryoshka TODO

    We will need to implement the algorithms described in the report.
    """
    
    def __init__(self):
        self.starting_value = 1

    def next_value(self):
        self.starting_value += 1
        return self.starting_value
