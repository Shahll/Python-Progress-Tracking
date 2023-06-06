str1 = "Worry"
str2 = "Mark"
str3 = ""

for i in range(2):
    str3 += str1[i]
for j in range(len(str2) - 2, len(str2)):
    str3 += str2[j]

print(str3)