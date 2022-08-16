from typing import Union
import math_parser
import errors

class Interpreter:

    def visit(self, node: math_parser.Node) -> Union[int, float]:
        if isinstance(node, str):
            result = float(node.split(":")[1])

        else:
            result = getattr(self, f"visit_{self.token_type(node.operation).lower()}")(node)
        return int(result) if result == int(result) else result

    def visit_plus(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_minus(self, node):
        return float(self.visit(node.left)) - float(self.visit(node.right))

    def visit_div(self, node):
        result = float(self.visit(node.right))
        if not result:
            raise errors.DivisionByZero("Can't divid a number by zero")
        return float(self.visit(node.left)) / result

    def visit_mult(self, node):
        return float(self.visit(node.left)) * float(self.visit(node.right))

    def visit_modulo(self, node):
        result = float(self.visit(node.right))
        if not result:
            raise errors.DivisionByZero("Can't divid a number by zero")
        return self.visit(node.left) % result

    def visit_eucl_div(self, node):
        result = float(self.visit(node.right))
        if not result:
            raise errors.DivisionByZero("Can't divid a number by zero")
        return float(self.visit(node.left)) // float(result)

    def token_type(self, token: str) -> str:
        return token.split(":")[0]