from parsing.tokens import Token



def tokenizeLines(lines):
  tokenizedLines = []
  for line in lines:
    tokenizedLines.append(
      [Token(t) for t in line]
    )
  return tokenizedLines