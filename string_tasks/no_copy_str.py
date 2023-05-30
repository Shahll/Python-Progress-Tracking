def no_copy(str1):
    c = 0
    double = []
    array = str1.split()
    for i in array:
        c = 0
        while c != str1.count(i) and str1.count(i) >= 2:
            array.remove(i)
            double.append(i)
            c += 1
    print(array, double)
    
str1 = "abc abc dcd dcd dcd abc fbe abeme abeme xuy xuy xuy xuy pidr abc"
no_copy(str1)
