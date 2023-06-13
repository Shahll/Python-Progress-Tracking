# Define lists for digit names
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# Function to convert a two-digit number into English
def convert_two_digits(num):
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    else:
        return tens[num // 10] + " " + ones[num % 10]

# Function to convert a four-digit number into English
def convert_four_digits(num):
    if num == 0:
        return "zero"
    else:
        thousands = ones[num // 1000] + " thousand " if num >= 1000 else ""
        hundreds = ones[(num // 100) % 10] + " hundred " if num >= 100 else ""
        two_digits = convert_two_digits(num % 100)
        return thousands + hundreds + two_digits

# Loop through numbers from 0 to 9999 and print the English translation
for num in range(10000):
    english = convert_four_digits(num)
    print(english)
