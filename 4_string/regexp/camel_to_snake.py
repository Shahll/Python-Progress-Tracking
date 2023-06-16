import re

text = "someTextInSnakeNotation"

modified_text = re.sub(r"([A-Z])", r"_\1", text).lower()
print(modified_text)