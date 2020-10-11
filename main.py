#!/bin/python
"""
main.py
=======
Run all matryoshka tests
"""

from random import choice

from src.Instrumentation import Instrumentation
from src import Matryoshka
from tests import *


MAX_TEST_LENGTH = 100
SEED = None


if __name__ == "__main__":
    # Run tests
    for test in all_tests:
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

            if test.visited_all_branches(test_inst):
                break
        print(
            f"Our Matryoshka visited {test_inst.num_branches()}/"
            f"{test.branches} branches"
        )
        # TODO compare with thefuzzingbook greyboxfuzzer
        print(f"test \"{test}\" finished\n")
        
