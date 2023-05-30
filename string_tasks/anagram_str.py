def is_anagram(string, string2):
    string = sorted(list(string))
    string2 = sorted(list(string2))
    return "They are an anagram" if string == string2 else "They are not an anagram"
# Driver    
str1 = "listen"
str2 ="silten"
print(is_anagram(str1, str2))