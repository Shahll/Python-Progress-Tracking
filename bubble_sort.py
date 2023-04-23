def bubble_sort(array):
    n = len(array)

    # We go through all numbers or digits in the list
    for i in range(n):


        # n = Numbers of out list 
        # i = quantity of numbers that already sorted and stay in their place
        # minus one because after running command we have one more sorted number
        for j in range(0, n-i-1):

            # Looking if first number is greater than second
            # Swapping it if True
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    # Return the sorted array
    return array

   