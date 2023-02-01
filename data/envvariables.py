

class EnvironmentHandler():
  def __init__(self):
    self.variables = {}

    self.testing()


  def testing(self):
    print("Info: You have testing environmentVariables turned on")
    
    self.variables["detailedPythonErrors"] = True

  
  def readVariable(self, name):
    try:
      return self.variables[name]
    except Exception:
      return None


  def writeVariable(self, name, value):
    self.variables[name] = value





environmentHandler = EnvironmentHandler()