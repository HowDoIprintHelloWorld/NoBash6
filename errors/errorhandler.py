from data.envvariables import environmentHandler


def warnPython(error):
  if environmentHandler.readVariable("detailedPythonErrors"):
    print(error)