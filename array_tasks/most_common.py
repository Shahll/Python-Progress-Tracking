""" 
    Знайти число у списку яке найбільше повторюється. 
    [ 1, 1, 1, 2, 2, 4, 4, 4, 4, 4] -> 4 
"""
lst = [ 1, 1, 1, 2, 2, 4, 4, 4, 4, 4]
most_common_number = max(set(lst), key = lst.count)
print(f"array: {lst}\nmost common number in array is: {most_common_number}")

    