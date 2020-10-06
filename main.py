#!/bin/python
"""
main.py
=======
Run all matryoshka tests
"""

from src.Instrumentation import Instrumentation
from src.Matryoshka import Matryoshka

from tests import *

MAX_TEST_LENGTH = 100


if __name__ == "__main__":
    # Run tests
    for test in all_tests:
        print(f"Starting test \"{test}\"")
        test_inst = Instrumentation()
        test_mat = Matryoshka() # TODO implement matryoshka
        for i in range(MAX_TEST_LENGTH):
            value = test_mat.next_value()
            test(value, test_inst)
            # TODO also test with thefuzzingbook greybox fuzzer
            if test.visited_all_branches(test_inst):
                break
        print(f"Our Matryoshka visited {test_inst.num_branches()}/"
              f"{test.branches} branches")
        # TODO compare with thefuzzingbook grayboxfuzzer
        print(f"test \"{test}\" finished\n")
        
