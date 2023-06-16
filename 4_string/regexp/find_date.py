import re

text = " ; dsadas asdasd asd 2022-01-22 adasd ads sa 2023-04-23"

date = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)

print(date)
