def counting_letters(str1):
    array_lower = [0] * 26 # отчет от 97 до 122  
    array_upper = [0] * 26 # отчёт от 65 до 90  

    for char in list(str1):
        if char == char.lower():
            array_lower[ord(char) - 97] += 1
        if char == char.upper():
            array_upper[ord(char) - 65] += 1
    result = [chr(index + 97) for index, value in enumerate(array_lower) for i in range(value)]
    
    print([(letter, result.count(letter)) for letter in set(result)])

    print("\n") 
    result = [chr(index + 65) for index, value in enumerate(array_upper) for i in range(value)]
    
    print([(letter, result.count(letter)) for letter in set(result)])
    
str1 = "abbcdejduiPONyanudBEBRAgaDADtfyoag"
counting_letters(str1)
