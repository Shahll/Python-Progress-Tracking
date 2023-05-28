def remake_text(str1):
    while "_" in str1:  
        temp = str1.find("_")
        str1 = str1[:temp] + str1[temp+1:]
        str1 = str1[:temp] +  str1[temp].upper() + str1[temp+1:]
    
    print(str1)
# Driver
str1 = "some_text_in_snake_notation"
remake_text(str1)