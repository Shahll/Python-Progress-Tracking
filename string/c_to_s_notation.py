def remake_text1(string):
    for index, char in enumerate(str1):
        if char.isupper():
            str1 = str1[:index].lower() + "_" + str1[index:]
            
    return string
# Driver
str1 = "someTextInSnakeNotation"
remake_text1(str1)
