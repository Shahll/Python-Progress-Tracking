import re

text = "Lina Kostenko (b. 19 March 1930)"

words = re.findall(r'\b[^\d\W]+\b', text)
print(words)