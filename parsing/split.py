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
If the letter is space or newline put append the previous tokenHolder to current line
If the letter is in splitters append the theprevious tokenHolder to currentline and this letter
Otherwise just append the letter to tokenHolder

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




def appendLine(lines, currentLine, tokenHolder):
  tokenHolder = appendToken(currentLine, tokenHolder)
  lines.append(currentLine)
  return [], tokenHolder

  
def appendToken(currentLine, tokenHolder):
  if tokenHolder:
    currentLine.append(tokenHolder)
  return ""


def iterLetters(text):
  lines = [] # Finished file split
  tokenHolder = "" # temporary holder for unfinished token
  currentLine = [] # holder for line
  appendMode = True
  previousDash = False
  commentMode = False
  
  for letter in text:
    if commentMode:
      if letter in ["\n", ";"]:
        commentMode = False  
      continue

    if letter == '"':
      appendMode = not appendMode
      if not appendMode:
        tokenHolder = appendToken(currentLine, tokenHolder)
      
      tokenHolder += letter
      previousDash = False
    
      
    # Adds to the token, and essentially invalidates all checks for newlines, comments etc
    elif not appendMode:
      tokenHolder += letter

    # Handles comments. Simply skips to the next line if there were two '/'
    elif letter == "/":
      if previousDash:
        currentLine, tokenHolder = appendLine(lines, currentLine, "")
        commentMode = True
        previousDash = False
      else:
        previousDash = True
      
    # Makes a new line if theres a newline character or a semi-colon
    elif letter in ["\n", ";"]:
      currentLine, tokenHolder = appendLine(lines, currentLine, tokenHolder)
      continue
      
    # Finishes token if theres a space
    elif letter == " ":
      tokenHolder = appendToken(currentLine, tokenHolder)
    
    # Simply adds the current letter to the temporary token
    else:
      tokenHolder += letter

  appendLine(lines, currentLine, tokenHolder)
  
  return lines



def split(text):    
  text = replace(text)
  text = addSpaces(text)
  lines = iterLetters(text)
  
  return lines