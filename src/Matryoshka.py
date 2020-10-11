"""
"""

from random import choice
from itertools import combinations

# https://python-algorithms.readthedocs.io/en/stable/_modules/python_algorithms/basic/union_find.html
from python_algorithms.basic.union_find import UF

from .Instrumentation import Instrumentation


def arg_count(f):
    """
    Returns number of arguments required for function.
    """
    return f.__code__.co_argcount

def get_args(original, indexes, new):
    assert len(indexes) == len(new)
    final_list = list(original)
    for index in indexes:
        final_list[index] = new[0]
        new = new[1:]
    return final_list

def find_effective_prior_cond_stmt(
        test,
        new_conditional,
        last_conditionals
):
    """
    algorithm1
    ==========
    new_conditional is a boolean function of a conditional we can evaluate.
    last_conditionals is a list of Functions accumulated so far.
    Returns: effective prior conditional statements of new_conditional
    Basically: returns a list of branches that matter
    """
    O = set()
    uf = UF(test.arguments)
    bs = None
    for statement in last_conditionals:
        T = statement.args
        for t1 in T:
            for t2 in T:
                if t1 != t2:
                    uf.union(t1, t2)
                    bs = new_conditional.args[0]
    if bs is None:
        return []
    for statement in last_conditionals:
        b = statement.args[0]
        if uf.find(bs) == uf.find(b):
            O.add(statement)
    return list(O)

def find_input(
        test,
        instrumentation,
        new_conditional,
        last_conditionals,
        *args
):
    """
    Find if input can be possibly changed to satisfy branch condition.
    """
    last_conditionals = last_conditionals.copy()
    
    # Forward phase
    all_possibilities = set([
        tuple(combo) for combo in combinations(
            range(2**8), len(new_conditional.args)
        )
    ])
    i = all_possibilities.pop()
    while (not new_conditional(
            instrumentation, get_args(args, new_conditional.args, i)
    ) and len(all_possibilities) > 0):
        i = choice(list(all_possibilities))
        all_possibilities.remove(i)
        passed = True
        new_inst = instrumentation.new()
        test(new_inst, get_args(args, new_conditional.args, i))
        if new_conditional.name in new_inst.conditional_to_count:
            return (True, i)

    # Backtracking phase
    B1 = set()
    backwards_conditionals = list(reversed(last_conditionals))
    for statement in backwards_conditionals:
        B = set(statement.args)
        B2 = (B - B1).pop()
        all_possibilities = set([
            tuple(combo) for combo in combinations(
                range(2**8), len(statement.args)
            )
        ])
        for j in all_possibilities:
            inst = Instrumentation()
            test(inst, get_args(args, statement.args, j))
            if statement in inst.current_run:
                return (True, j)
        B1.union(B)
    return (False, -1)
