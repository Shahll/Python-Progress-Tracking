import re

text = """ 
Телефонний номер Євгена +38-(09)-1234567. 
Він дуже схожий на телефонний номер Тетяни (097)-1234567
але геть інакший від номера Дмитра 050-7654321. 
"""

numbers = re.findall(r"((\+\d{1,4}-)?((\(\d{1,3}\))|(\d{1,3}))-\d{7})", text)

numbers = [match[0] for match in numbers]

print(numbers)