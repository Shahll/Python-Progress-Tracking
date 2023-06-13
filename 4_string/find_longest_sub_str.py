""" 
Find the longest continuous substring 
"""
def longest_substr(string):
    longest = 0
    char = string[0]
    for i in set(list(string)):
        if longest < string.find(i):
            longest = string.find(i)
            char = i
            
    print(f"Letter '{char}' was find {longest} times")
    
    
str1 =  "abbbccdddddddxxxxxxxxxxx"
longest_substr(str1)