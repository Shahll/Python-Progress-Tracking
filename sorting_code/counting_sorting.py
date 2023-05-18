lst = [17, 0, 8, 20, 12, 13, 2, 4, 17, 18, 18, 16, 8, 3, 20, 2, 9, 17, 17, 12]
counting_lst = [0]
sorted_lst = []

for _ in lst:
    counting_lst.append(0)
    sorted_lst.append(0)
    
def assign_numbers(list_to_assign, counting_list):
    for assign in list_to_assign:
        counting_list[assign] += 1
    return counting_list


def adding_numbers(list_to_add):
    for add in range(1, len(list_to_add)):
        list_to_add[add] += list_to_add[add - 1]
    return list_to_add


def counting_sort(list_to_sort, counting_list,sorted_list,):
    for assign in range(len(list_to_sort) - 1, -1, -1):
        index_search = list_to_sort[assign]
        temp = counting_list[index_search]
        counting_list[index_search] -= 1
        sorted_list[temp - 1] = list_to_sort[assign]
    return sorted_list



counting_lst = assign_numbers(lst,counting_lst)
counting_lst = adding_numbers(counting_lst)
sorted_lst = counting_sort(lst,counting_lst,sorted_lst)

print(sorted_lst)

