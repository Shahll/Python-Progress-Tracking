def is_anagram(string, string2):
    return sorted(list(string)) == sorted(list(string2))

# Driver    
str1 = "listen"
str2 ="silten"
print(is_anagram(str1, str2))
