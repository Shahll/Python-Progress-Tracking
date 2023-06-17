import re

text = "https://bebra.com htpp   http://dad https/:"

url = re.findall(r"https?://\w+\.\w+", text)

print(url)