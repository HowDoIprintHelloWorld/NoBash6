
from parsing.tokens.token import Token


class Bool(Token):
  def __init__(self, value):
    super().__init__(value)
    self.value = bool(self.value)

