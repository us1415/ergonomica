"""
[operator.py]

"""

# pylint doesn't know that this file will be imported from ../../ergonomica
# pylint: disable=import-error

import re
import traceback

from lib.lang.error_handler import ErgonomicaError

def get_operator(string):
    """Find functional-programming operators in a string.
       e.g., get_operator("(map) x + 3")       = "map"
             get_operator("(filter) x == '1'") = "filter".
    """
    print "string is", string
    operators = ["map", "filter", "match", "reverse", "splice"]
    try:
        operator = re.match(r"\([A-z]*\)", string.strip()).group()[1:-1]
        if operator in operators:
            return operator
        else:
            raise ErgonomicaError
    except AttributeError:
        traceback.print_exc()
        return False