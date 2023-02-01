from iohandler.readscript import readscript
from data.envvariables import environmentHandler

from parsing.split import split
from parsing.tokenizeLines import tokenizeLines





if __name__ == "__main__":
  text = readscript("test.ns")   # For now, just read test file
  stringLines = split(text)  # Turn the string into a 2D strings-list
  lines = tokenizeLines(stringLines)
  
  print(lines)