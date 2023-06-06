def counter(string):
    print(f"In text ({string}):\n")
    print(f"Uppercase letters:", sum(1 for i in string if i.isupper()))
    print(f"Lowercase letters:", sum(1 for i in string if i.islower()))
    print(f"Number letters:", sum(1 for i in string if i.isnumeric()))
    print(f"Spacebar letters:", sum(1 for i in string if i.isspace()))
    
str1 = "PipiSka_ 228 cool"
counter(str1)