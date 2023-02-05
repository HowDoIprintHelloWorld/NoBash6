from parsing.tokens.token import Token


class Int(Token):
  def __init__(self, value):
    super().__init__(value)
    self.value = int(self.value)

