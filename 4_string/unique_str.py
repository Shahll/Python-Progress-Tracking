def unique_characters(string):
    used = []
    return [char for char in string if char not in used and (used.append(char) or True)]
# Driver
str1 = "Hello"
print(unique_characters(str1))