#!/usr/bin/env python3

import sys
from typing import List



class RpnEvaluator:
    ops = {
        '+': lambda l, r: l + r,
        '-': lambda l, r: l - r,
        '*': lambda l, r: l * r,
        '/': lambda l, r: int(l / r),
    }
    stack: List[int]

    def __init__(self):
        self.stack = []

    def eval(self, expr: List[str]) -> int:
        for e in expr:
            try:
                op = RpnEvaluator.ops[e]
                rhs = self.stack.pop()
                lhs = self.stack.pop()
                self.stack.append(op(lhs, rhs))
            except KeyError:
                self.stack.append(int(e))

        return self.stack.pop()


def evaluate_reverse_polish_notation(expr: List[str]) -> int:
    raise "to be implemented"

def main(argv: List[str]):
    evaluate_reverse_polish_notation(argv)


if __name__ == '__main__':
    main(sys.argv)
