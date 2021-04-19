## ----- BALANCED NUMBERS ----
## 
## TASK CONDITIONS:
#  1. Take input from user. Only 3 digit numbers and--
#  2. -- only digits where the sum of the 1st and 3rd digit is equal to the 2nd digit. 
#  3. Iteration stops when an invalid 3 digit number is entered:
#     - invalid digit is a digit where [0] + [2] != [1]
#     - display the sum of all three digit numbers that have previously passed/been accepted
#  
#    INPUT:
#     275 
#     693
#     110
#     742
#    OUTPUT:
#     1078

def balanced_numbers():
    total_sum = 0
    condition = False
    while not condition:
        get_num = input('Enter 3 digits. Sum of 1st and 3rd should be equal to the 2nd: ')
        if get_num.isdigit():
            if len(get_num) == 3:
                the_sum = int(get_num[0]) + int(get_num[2])
                second = int(get_num[1])

                if the_sum == second:
                    total_sum += int(get_num)
                else:
                    print(total_sum)
                    condition = True
            else:
                print('We need a whole 3 digit number, please.')
        else:
            print('Numbers only, please.')
    

if __name__=='__main__':
    balanced_numbers()