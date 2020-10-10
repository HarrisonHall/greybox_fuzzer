# Matryoshka Greybox Fuzzer
CPSC 4200 Python Implementation of Matryoshka

## Execution
Run `python main.py` to execute all tests.

## Code
* `src/Instrumentation` provides a class to track instrumentation
* `src/Matryoshka` provides our implementation of matryoshka
* `tests` holds all tests we've written with various branching behaviors
* `tests/Test` provides a class to make tests

## TODO
* Create more tests
  * Tests with multiple variables
  * Deeper nested branches
* Implement matryoshka
* Integrate thefuzzingbook greybox fuzzer for comparison
* Maybe use argparse to make the tool usable on other programs?
  * This may be very difficult and isn't necessarily something we need to do
	* Difficulty in using with other programs, not with argparse obv
  * Might make for a nice grade tho
* Seed runs
* Mutate input instead of randomizing it
