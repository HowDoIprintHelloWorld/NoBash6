"""
Task: 
Given an input file, split up the text into:
-> lines
  -> individual untokenzied parts


Why:
Make the script ready for lexical analysis


Approach:
Replace things like '**' with ' pow ' and '==' with ' iseq '



Go through each letter
Have a list of "splitters" 
If the letter is a '"', then switch 'appendmode' on or off


If the letter is newline or ';', make a new line
If the letter is space or newline put append the previous tokenline to current line
If the letter is in splitters append the theprevious tokenline to currentline and this letter
Otherwise just append the letter to tokenline

"""
REPLACERS = {"**":" pow ", "==": " iseq "}
SPLITTERS = {"*":"lr", "+":"lr", "/":"lr", "-":"lr", "(":"lr", ")":"lr"}   # {sign: where to split (left/right/both)}


def replace(text):
  for old, new in REPLACERS.items():
    text = text.replace(old, new)
  return text


def addSpaces(text):
  for splitter, locations in SPLITTERS.items():
    replace = splitter
    if "l" in locations:
      replace = " "+replace
    if "r" in locations:
      replace = replace+" "
    text = text.replace(splitter, replace)
  return text




def appendLine(lines, tmpline, tokenline):
  tokenline = appendToken(tmpline, tokenline)
  lines.append(tmpline)
  return [], tokenline

  
def appendToken(tmpline, tokenline):
  if tokenline:
    tmpline.append(tokenline)
  return ""


def iterLetters(text):
  lines = [] # Finished file split
  tokenline = "" # temporary holder for unfinished token
  tmpline = []
  appendMode = True
  
  for letter in text:
    if letter == '"':
      appendMode = not appendMode
      if not appendMode:
        tokenline = appendToken(tmpline, tokenline)
      
      tokenline += letter
      
    elif not appendMode:
      tokenline += letter
      
    elif letter in ["\n", ";"]:
      tmpline, tokenline = appendLine(lines, tmpline, tokenline)
      continue
      
    elif letter == " ":
      tokenline = appendToken(tmpline, tokenline)
      
    else:
      tokenline += letter

  appendLine(lines, tmpline, tokenline)
  
  return lines



def split(text):    
  text = replace(text)
  text = addSpaces(text)
  lines = iterLetters(text)
  
  return lines