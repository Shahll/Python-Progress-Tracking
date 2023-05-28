def polindrom(str1):
    if str1 == str1[:: - 1]:
        return True
    else:
        return False
    
def polindrom_loop(str1):
    s = ""
    for i in range(len(str1)-1, -1, -1):
        s += str1[i]
    if s == str1:
        return True
    else:
        return False
    
# Driver
str1 = "aboba"    
print(polindrom_loop(str1))
