from data.envvariables import environmentHandler
from errors.errorhandler import warnPython


def readscript(filename):
  try:
    with open(filename, "r") as f:
      return f.read()

  except Exception as e:
    print(f"Can't open file '{filename}'")
    warnPython(e)
    