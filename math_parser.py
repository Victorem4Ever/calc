from typing import Union
import errors

class Parser:
    def __init__(self, tokens: list[str]) -> None:
        self.tokens = tokens
        self.token  = tokens[0]
        self.index  = 0

        self.operators = [
            "MULT",
            "PLUS",
            "MINUS",
            "DIV",
            "EUCL_DIV",
            "MODULO"
        ]
    
    def parse(self):
        return self.expression()

    def advance(self) -> None:
        if self.index >= len(self.tokens) - 1:
            self.token = None
            return
        
        self.index += 1
        self.token = self.tokens[self.index]

    def token_type(self, token=None) -> str:
        token = self.token if token is None else token
        if token is None:
            return
        return token.split(":")[0]

    def factor(self) -> Union[str,None]:
        if self.token_type() in ("INT", "FLOAT"):
            token = self.token
            self.advance()
            return token

        elif self.token_type() == "OPEN_PAREN":
            self.advance()
            result = self.expression()

            if self.token_type() != "CLOSE_PAREN":
                raise errors.SyntaxError("Parenthese not closed")

            self.advance()
            return result
        
        else:
            return "INT:0"

    def expression(self) -> None:
        return self.binary_operation(self.term, ("PLUS", "MINUS"))

    def term(self) -> None:
        return self.binary_operation(self.factor, ("DIV", "MULT", "EUCL_DIV", "MODULO"))

    def binary_operation(self, function: callable, operations: Union[tuple, list]) -> Union[int, float, "Node"]:

        left = function()
        while self.token_type() in operations and self.token is not None:
            operation_token = self.token
            self.advance()

            if self.token_type() in self.operators:
                print(self.token_type())
                raise errors.SyntaxError("can't use two operators in a row")
                
            right = function()

            if right is None:
                raise errors.SyntaxError("last char must be a number, not an operator")
            left = Node(left, operation_token, right)

        return left

class Node:
    def __init__(self, left_node: Union[str, "Node"], operation, right_node: Union[str, "Node"]) -> None:
        self.left = left_node
        self.right = right_node
        self.operation = operation

    def __repr__(self) -> str:
        return f'({self.left}, {self.operation}, {self.right})'