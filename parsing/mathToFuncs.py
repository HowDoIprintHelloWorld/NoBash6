from parsing.tokens.operatorToken import Operator
from parsing.tokens.functionToken import Function

"""
Task:
On previous attemtps, working with math has always proven to be annoying. My idea is to, instead of scanning the line for powers, then times/divided, then add/sub and calculating those, since that can cause errors when adding to a function, we turn the operands and the to-be-operated-on numbers into a function call. Heres an example:
put(1 + 2) -> put(add(1, 2))
(1 + 3) * 4 -> mul(add(1, 3), 4)

Why:
As previously stated, figuring out edge cases of what to calculate fist: the function or the addition, what if they are a parameter etc drives me up the walls. As such, now there is only one "order" in which I have to calculate: the leftmost innermost bracket is always claculated first

Approach:
Do all of this in the order of operations:
-> find the current operation
-> check if the token to the left or right is a bracket (and in the case of right also function!!!)
  -> if so, move over further until you find an opening/closing bracket
-> At this spot, set a closing/opening bracket with a corresponding function call

"""

OPSWITHFUNC = [{"pow":"pow"}, {"*":"mul", "/":"div"}, {"+":"add", "-":"sub"}]
OPSWITHFUNCTOGETHER = {"pow":"pow", "*":"mul", "/":"div", "+":"add", "-":"sub"}
OPS = [list(part.keys()) for part in OPSWITHFUNC]


def checkValidIndex(index, lineLen, line):
  works =  index > 0 and index < lineLen-1
  if not works:
    print("Error: operator at weird location")
    print(index, lineLen, line)


def iterateLine(line, operandList):
  lineLength = len(line)
  for index, token in enumerate(line):
    
      # print("Op:", token.value, "List:",operandList)      
      # ¨print("OP in list:", token.value in operandList)
      if token.value in operandList:
        checkValidIndex(index, lineLength, line)
        line[index] = Operator(",")
        line.insert(index-1, Function(OPSWITHFUNCTOGETHER[token.value]))
        line.insert(index, Operator("("))
        line.insert(index+4, Operator(")"))
  
  return line


def mathToFuncs(line):
  for operandList in OPS:
    line = iterateLine(line, operandList)
  print("line: ", line)
  return line
        



  