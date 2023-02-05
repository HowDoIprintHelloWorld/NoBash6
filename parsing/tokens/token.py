from parsing.detectType import detectType

"""
Task:
Create a token class. All tokens should be of this type, be it an opening bracket in a function call or a string. The token can automatically detect its own type. This class is just a base-item, and there are individual classes for each type with its own functions depending on its case (i.e: Add function for ints)

Why:
This is a core concept of a programming language, and as such, it is imperative that it is both functional and reliable. Every part of this lanugage is a token.

Approach:
The token object needs the following:
- a type
- a value

- a detection function




"""



class Token():
  def __init__(self, value):
    self.value = value
    self.type = "none"

    self.detect() 


  
  def detect(self):
    self.type = detectType(self.value)
  

  def __str__(self):
    return f"{self.value}"# {self.type[:2]}"

  def __repr__(self):
    return f"{self.value}"# ({self.type[:2]})"