import errors

class Lexer:
    def __init__(self, code) -> None:
        self.code = code
        if len(code.split("\n")) > 1:
            raise errors.WrongCodeFormat("Code has to be oneline only")

        elif not code.strip():
            raise errors.WrongCodeFormat("Code can't be spaces only")

        opened = code.count("(")
        closed = code.count(")")
        if opened > closed:
            raise errors.WrongParentheseUsage(f"{opened - closed} parenthese(s) never closed")

        elif closed > opened:
            raise errors.WrongParentheseUsage(f"{closed - opened} parenthese(s) never opened")

    def make_tokens(self) -> None:
        """
        Possibles tokens :
            BLANK
            INT
            FLOAT
            PLUS
            MINUS
            DIV
            EUCL_DIV
            MULT
            MODULO
            OPEN_PAREN
            CLOSE_PAREN
        """
        self.tokens = []
        self.char = self.code[0]
        self.current_pos = 0
        while self.char is not None:

            if self.char.isspace():
                # self.make_space()
                self.advance()

            elif self.char.isdecimal():
                self.make_number()

            elif self.char == "+":
                self.tokens.append("PLUS")
                self.advance()

            elif self.char == "-":
                self.tokens.append("MINUS")
                self.advance()

            elif self.char == "/":

                token = "DIV"
                self.advance()
                if self.char == "/":
                    token = "EUCL_DIV"
                    self.advance()
                self.tokens.append(token)
                

            elif self.char in ("x", "*"):
                self.tokens.append(f"MULT:{self.char}")
                self.advance()

            elif self.char == "%":
                self.tokens.append("MODULO")
                self.advance()

            elif self.char == "(":
                self.tokens.append("OPEN_PAREN")
                self.advance()

            elif self.char == ")":
                self.tokens.append("CLOSE_PAREN")
                self.advance()

            else:
                raise errors.UnknownChar(f"Char '{self.char}' can't be used")

    def advance(self) -> None:
        if self.current_pos >= len(self.code) - 1:
            self.char = None
            return
        
        self.current_pos += 1
        self.char = self.code[self.current_pos]

    """
    def make_space(self) -> None:
        spaces = ""
        while self.char is not None and self.char.isspace():
            spaces += self.char
            self.advance()

        self.tokens.append(f"BLANK:{spaces}")
    """

    def make_number(self) -> None:
        number = ""
        dot = False
        while self.char is not None:
            if self.char.isdecimal():
                number += self.char
            elif not dot and self.char == ".":
                number += self.char
                dot = True
            
            else:
                break
            
            self.advance()

        self.tokens.append(f"{'FLOAT' if dot else 'INT'}:{number}")