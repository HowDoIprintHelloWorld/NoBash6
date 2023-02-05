
from parsing.tokens.token import Token


class Float(Token):
  def __init__(self, value):
    super().__init__(value)
    self.value = float(self.value)

