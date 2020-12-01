#!/bin/python
"""
main.py
=======
Run all matryoshka tests
"""

from random import choice
from copy import deepcopy

# Matryoshka
from src.Instrumentation import Instrumentation
from src import Matryoshka
from src.Logger import Logger
from tests import *

# FuzzingBook
from src.TFB import TFBFuzzer


MAX_TEST_LENGTH = 100
SEED = None


if __name__ == "__main__":
    # Run tests
    all_tests1 = [test.copy() for test in all_tests]
    for test in all_tests1:
        l = Logger()
        print(f"Starting test \"{test}\"")
        test_inst = Instrumentation()
        for i in range(MAX_TEST_LENGTH):
            generate_input = True
            test_inst.reset_run()
            if generate_input:
                args = []
                for j in range(test.arguments):
                    args.append(choice(range(2**8)))
            test(test_inst, args)

            if test_inst.current_failures:
                conditionals = Matryoshka.find_effective_prior_cond_stmt(
                    test,
                    test_inst.current_failures[0],
                    test_inst.current_run
                )
                dont_generate_input, inputs = Matryoshka.find_input(
                    test,
                    test_inst,
                    test_inst.current_failures[0],
                    test_inst.current_run,
                    *args
                )
                generate_input = not dont_generate_input
                if dont_generate_input:
                    if isinstance(inputs, int):
                        inputs = [inputs] 
                    args = Matryoshka.get_args(args, test_inst.current_failures[0].args, inputs)

            l.log(i, test_inst.num_branches())
            
            if test.visited_all_branches(test_inst):
                break
            
        print(
            f"Our Matryoshka visited {test_inst.num_branches()}/"
            f"{test.branches} branches"
        )
        #print(l)
        print(f"test \"{test}\" finished\n")

    # Run tests
    all_tests2 = [test.copy() for test in all_tests]
    for test in all_tests2:
        print(f"Starting test \"{test}\"")
        test_inst = Instrumentation()
        l = Logger()
        
        generate_input = True
        for i in range(MAX_TEST_LENGTH):
            test_inst.reset_run()
            if generate_input:
                args = []
                for j in range(test.arguments):
                    args.append(choice(range(2**8)))
                generate_input = False
            else:
                for j in range(len(args)):
                    args[j] = TFBFuzzer(args[j]).mutate()
            
            test(test_inst, args)
            l.log(i, test_inst.num_branches())

            if test.visited_all_branches(test_inst):
                break
            
        print(
            f"TheFuzzingBook's AFL MutationFuzzer visited {test_inst.num_branches()}/"
            f"{test.branches} branches"
        )
        #print(l)
        # TODO compare with thefuzzingbook greyboxfuzzer
        print(f"test \"{test}\" finished\n")
        
