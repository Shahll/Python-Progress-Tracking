def fix_str(str1):
    str1 = str1.split()
    i = 0
    while i != len(str1) - 1:
        i += 1
        if len(str1[i]) <= 3:
            str1.pop(i)
            i -= 1
        elif str1[i].isnumeric() == True:
            str1.pop(i)
            i -= 1
            
    str1 = ', '.join(str1)
    print(str1)
    
    
    
str1 = """ 
алфАвІт 

ц

кОпчений 12

т

веснЯнИй  п

в

перенестИ в

1
"""
fix_str(str1)
