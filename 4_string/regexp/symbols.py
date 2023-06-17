import re

text = "Ліна Василівна @Кос$тенко (нар. 19 березня 1930),! "

symbols = re.findall(r"[^\w\s]", text)

print(symbols)  # Output: ['@', '$', '(', ')', ',', '!']
