class WrongParentheseUsage(Exception):
    """
    Raise when parentheses aren't closed or opened correctly
    """

class WrongCodeFormat(Exception):
    """
    Raise when the code format isn't correct
    """

class UnknownChar(Exception):
    """
    Raise when a char is unknown
    """

class SyntaxError(Exception):
    """
    Raise when the syntax isn't correct
    """

class DivisionByZero(Exception):
    """
    Raise when a number is divided by zero
    """