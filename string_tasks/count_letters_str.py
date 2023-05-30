from collections import Counter

def counting_letters(str1):
    array_lower = [0] * 26 # отчет от 97 до 122  
    array_upper = [0] * 26 # отчёт от 65 до 90  

    for char in list(str1):
        if char == char.upper():
            array_upper[ord(char) - 65] += 1
        if char == char.lower():
            array_lower[ord(char) - 97] += 1
    result = [f"{chr(index + 97)}" for index, value in enumerate(array_lower) for i in range(value)]
    result = Counter(result)
    
    for item, count in result.items():
        print(f"{item}: {count}")
        
    print("\n") 
    result = [f"{chr(index + 65)}" for index, value in enumerate(array_upper) for i in range(value)]
    result = Counter(result)
    for item, count in result.items():
        print(f"{item}: {count}")
    
str1 = "abbcdejduiPONyanudBEBRAgaDADtfyoag"
counting_letters(str1)