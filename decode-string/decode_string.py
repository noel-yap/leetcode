# ENC_STR := { EXPR }
# EXPR := [ NUM ] "[" EXPR "]"
from typing import Callable, Tuple

class Decoder:
    def __init__(self):
        self.stack = [""]

    def decode(self, encoded_str):
        return self.decode_expr(encoded_str)[0]

    def decode_expr(self, encoded_str, stop: Callable[[str], bool]=None) -> Tuple[str, str]:
        if stop is None:
            stop = lambda s: False

        while len(encoded_str) > 0:
            if stop(encoded_str[0]):
                return self.stack.pop(), encoded_str[1:]
            elif encoded_str[0].isdigit():
                decoded_str, encoded_str = self.decode_num_expr(encoded_str)
            elif encoded_str[0] == '[':
                return self.decode_bracket_expr(encoded_str)
            else:
                decoded_str, encoded_str = self.decode_str_expr(encoded_str)

            self.stack[-1] += decoded_str

        return self.stack[-1], encoded_str

    def decode_bracket_expr(self, encoded_str) -> Tuple[str, str]:
        self.stack.append("")

        return self.decode_expr(encoded_str[1:], stop=lambda s: s == ']')

    def decode_num_expr(self, encoded_str) -> Tuple[str, str]:
        n = 0
        i = 0
        while i < len(encoded_str) and encoded_str[i].isdigit():
            n *= 10
            n += int(encoded_str[i])
            i += 1

        decoded_str, encoded_str = self.decode_expr(encoded_str[i:])

        return decoded_str * n, encoded_str

    @staticmethod
    def decode_str_expr(encoded_str) -> Tuple[str, str]:
        i = 0
        while (i < len(encoded_str) and
               not encoded_str[i].isdigit() and
               encoded_str[i] != '[' and
               encoded_str[i] != ']'):
            i += 1

        return encoded_str[:i], encoded_str[i:]
