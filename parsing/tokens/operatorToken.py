
from parsing.tokens.token import Token


class Operator(Token):
  def __init__(self, value):
    super().__init__(value)
    self.value = str(self.value)

