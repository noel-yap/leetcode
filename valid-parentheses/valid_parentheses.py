#!/usr/bin/env python3

import sys
from typing import List


def valid_parentheses(v: str):
    stack = []
    for c in v:
        if c in ['(', '[', '{']:
            stack.append(c)
        elif c in [')', ']', '}']:
            if top_matches(stack, c):
                stack.pop()
            else:
                return False

    return len(stack) == 0


def matching_open_char(c: str):
    if c == ')':
        return '('
    elif c == ']':
        return '['
    elif c == '}':
        return '{'
    else:
        return None


def top_matches(stack: List[str], c: str):
    return len(stack) > 0 and stack[-1] == matching_open_char(c)


def main(argv: List[str]):
    for v in argv:
        print(valid_parentheses(v))


if __name__ == '__main__':
    main(sys.argv)
