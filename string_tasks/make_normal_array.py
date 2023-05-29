str1 = "1  ,  2  ,  3  ,  4  ,  5  ,  6  ,  7"
str1 = str1.replace(",", "")
print(list(map(int, str1.split( ))))
