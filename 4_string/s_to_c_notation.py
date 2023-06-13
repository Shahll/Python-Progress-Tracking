def remake_text(str1):
    parts = str1.split("_")
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

# Driver
str1 = "some_text_in_snake_notation"
print(remake_text(str1))
