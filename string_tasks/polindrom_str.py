def polindrom(str1):
    if str1 == str1[:: - 1]:
        return True
    else:
        return False
# Driver
str1 = "aboba"    
print(polindrom(str1))
