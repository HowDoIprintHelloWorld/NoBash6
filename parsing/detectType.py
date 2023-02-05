from data.datalist import OPERANDS

nums = "1234567890"



def detectType(inpt):
  if detectInt(inpt):
    return "int"
  elif detectFloat(inpt):
    return "float"
  elif detectOperator(inpt):
    return "operator"
  elif detectString(inpt):
    return "string"
  elif detectBool(inpt):
    return "bool"

  return "unknown"

def detectBool(inpt):
  return inpt in ["true", "false"]

def detectOperator(inpt):
  if inpt in OPERANDS: return True
  return False

def detectString(inpt):
  return inpt.startswith('"') and inpt.endswith('"')

def detectInt(inpt):
  return not [lett for lett in inpt if lett not in nums]

def detectFloat(inpt):  
  return not [lett for lett in inpt if lett not in nums+"."]