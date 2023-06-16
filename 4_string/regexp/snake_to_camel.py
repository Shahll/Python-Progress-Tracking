import re

def change_to_upper(match):
    return match.group(0).upper()

text = "some_text_in_snake_notation"

modified_text = re.sub(r"(_\w)", change_to_upper, text)
modified_text = re.sub(r"_", "", modified_text)

print(modified_text)
