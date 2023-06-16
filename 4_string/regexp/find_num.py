import re 

text = "Ліна Василівна Костенко (нар. 19 березня 1930)"
matches = re.findall(r"\d+", text)
print(matches)

