## ----- CROOKED NUMBERS ----
## 
## TASK CONDITIONS:
#  1. Clean all input of additional digits and formatting. Extract only the numbers.
#  2. Find sum of digits until the sum is a single digit.
#  
#    INPUT:
#    -123.0 
#    OUTPUT:
#     6


def single_digit():
    user_input = input('Enter a number, please: ')
    numeric_filter = filter(str.isdigit, user_input) #clean string of non-number values
    numeric_int = int(''.join(numeric_filter))

    while numeric_int > 9:
        sum_of_nums = 0
        for each in str(numeric_int):
            sum_of_nums += int(each)
        numeric_int = sum_of_nums
    
    print(numeric_int)


if __name__=='__main__':
    single_digit()




### ALTERNATIVELY
###   import re
###   a_string = "!1a2;b3c?"
###   numeric_string = re.sub("[^0-9]", "", a_string)
