def test(string):
    string = string.split(", ")
    num_q = len(string) // 3
    
    string[2] = string[2][1:-1]
    sub_string = string[2].split(" ")

    cur_q = 1
    nxt = 0
    correct = 0
    wrong = 0
    wrong_ans = []
    
    
    while True:
        print('\033[32m' + '\033[1m' + f"[{cur_q}/{num_q}]: {string[0 + nxt]} \n" + '\033[0m')
        for i in range(len(sub_string)):
            print('\033[34m' + '\033[1m' + f"{i + 1}: Вариант: {sub_string[i]}"  + '\033[0m' )
        user = int(input('\033[33m' + '\033[1m' + "Enter the number of the option you think is correct: " +  '\033[0m'))
        print("\n")
        if sub_string[user - 1] == string[1 + nxt]:
            correct += 1
        else:
            wrong += 1
            wrong_ans.append(sub_string[user - 1])
            wrong_ans.append(string[1 + nxt])
        cur_q += 1
        nxt += 3
        
        if cur_q -1 != num_q:
            string[2 + nxt] = string[2 + nxt][1:-1]
            sub_string = string[2 + nxt].split(" ")
        else:
            print('\033[1m' + '\033[31m'+ f"Your have {correct} correct answers and {wrong} wrong answers\n" + '\033[0m')
            if correct != cur_q -1:
                user = input('\033[32m' + '\033[1m' + "You want to see where you went wrong(yes/no): " +  '\033[0m')
                if user == 'yes':
                    for i in range(0, len(wrong_ans), 2):
                        print(f"You answered '{wrong_ans[i]}' but correct answer was '{wrong_ans[i + 1]}'")
            break
                    
                
                
""" 
it is very important that the first line is a question, the second line is the answer to the question, 
and the third line is written in square brackets and everything is written with a coma and a space 
"""           
str1 = "ти сидиш у кущах?, частково, [так ні частково], ти любиш солодке?, так, [так ні напевно]"
test(str1)