from parsing.tokens.token import Token
from parsing.tokens.intToken import Int
from parsing.tokens.floatToken import Float
from parsing.tokens.stringToken import String
from parsing.tokens.boolToken import Bool
from parsing.tokens.unknownToken import Unknown
from parsing.tokens.operatorToken import Operator

from parsing.mathToFuncs import mathToFuncs
from parsing.detectType import detectType

TYPES = {"int":Int, "unknown":Unknown, "float":Float, "string": String, "operator":Operator}

def makeToken(t):
  return TYPES[detectType(t)](t)



def tokenizeLines(lines):
  tokenizedLines = []
  for line in lines:
    line = [makeToken(t) for t in line]
    # line = mathToFuncs(line)
    tokenizedLines.append(line)
  return tokenizedLines