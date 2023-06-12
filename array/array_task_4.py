"""4. рівень __________
 а. Розвернути список 
    [ 1 2 3 4 5 ] -> [ 5 4 3 2 1 ]
 б. Змістити масив вліво 
    # Зробити власноруч та знайти функцію для цього
    [ 1 2 3 4 5 ] -> [ 2 3 4 5 0 ]
    [ 2 3 4 5 0 ] -> [ 3 4 5 0 0 ]
 в. Змістити масив вправо 
    # Зробити власноруч та знайти функцію для цього
    [ 1 2 3 4 5 ] -> [ 0 1 2 3 4 ] 
    [ 0 1 2 3 4 ] -> [ 0 0 1 2 3 ]
    г. Змістити масив циклічно вправо та вліво
    # Зробити власноруч та знайти функцію для цього
 Вліво:
    [ 1 2 3 4 5 ] -> [ 2 3 4 5 1 ]
    [ 2 3 4 5 0 ] -> [ 3 4 5 1 2 ]
 Вправо:  
    [ 1 2 3 4 5 ] -> [ 5 1 2 3 4 ] 
    [ 5 1 2 3 4 ] -> [ 4 5 1 2 3 ]
    """
    
    
"""
# вертим список в обратном порядке

array = [1,2,3,4,5]
reversed_array = array[::-1]
print(reversed_array)

"""



"""

# мой код чтобы сдвигать список в лево 
# P.s для этого как таковой функции я не нашёл только более простой код

array = [1,2,3,4,5]

array.insert(0, array[0] - 1)
for index, value in enumerate(array):

   if value == array[0]: 
      array.remove(value)   # записать len(array) - 1 в квадратных скобках чтобы код двигал список в право
      array.pop(0)
      array.append(value)   # заменить строку на array.insert(0, value) чтобы двигать список в право
      
      
print(array)  # вывод 2 3 4 5 0 если в лево и 0 1 2 3 4 если в право


"""




















"""
# использование функции чтобы сдвинуть список цыклично в лево (изменить число в dq.rotate на чтобы он двигал в право)

from collections import deque

array = [1,2,3,4,5]

dq = deque(array)
dq.rotate(-1)
array = list(dq)

print(array) # вывод 2 3 4 5 1
"""





"""

# мой написаный код чтобы сдвинуть список цыклично в лево

array = [1,2,3,4,5]


for index, value in enumerate(array):
   
   if value == array[0]: # записать len(array) - 1 в квадратных скобках чтобы код двигал список в право
      array.remove(value)
      array.append(value) # заменить строку на array.insert(0, value) чтобы двигать список в право

print(array) # вывод 2 3 4 5 1 если в лево и 5 1 2 3 4 если в право




"""
































