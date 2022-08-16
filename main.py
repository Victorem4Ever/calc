from lexer import Lexer
from math_parser import Parser
from interpreter import Interpreter
from typing import Union

def run(code: str) -> Union[int, float]:
    lexer = Lexer(code)
    lexer.make_tokens()
    return Interpreter().visit(Parser(lexer.tokens).parse())

if __name__ == "__main__":

    user_input = input("Calc: ")
    while user_input != "EXIT":
        try:
            print(run(user_input))
        except Exception as e:
            print(e)
        user_input = input("Calc: ")