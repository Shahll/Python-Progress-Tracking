def is_closed(string):
    while "()" in string or "[]" in string or "{}" in string:
        string = string.replace("()", "").replace("[]", "").replace("{}", "")
    return len(string) == 0
    
    
    
str1 = "{([])}"
print(is_closed(str1))