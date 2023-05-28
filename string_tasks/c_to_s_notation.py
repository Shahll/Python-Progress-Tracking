def remake_text(str1):
    j = -1
    for index, char in enumerate(str1):
        if char.isupper():
            j += 1
            str1 = str1.replace(char, char.lower())
            str1 = str1[:index + j] + "_" + str1[index + j:]
    print(str1)
# Driver
str1 = "someTextInSnakeNotation"
remake_text(str1)
