def length_str(str1):
    counter = 0
    for i in range(len(str1)):
        counter += 1
    return counter
# Driver
str1 = "aboba"
print(f"Lenght of the string is {length_str(str1)}")