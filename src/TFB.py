from fuzzingbook.MutationFuzzer import *
from random import randint


def flip_bit(i):
    return i ^ (1 << randint(0, 7))


class TFBFuzzer(MutationFuzzer):
    def __init__(self, seed, min_mutations=100, max_mutations=100):
        super().__init__(seed, min_mutations, max_mutations)
    
    def fuzz(self):
        # seed is byte integer
        new = flip_bit(self.seed)
        self.seed = new
        return new

    def mutate(self):
        return self.fuzz()


