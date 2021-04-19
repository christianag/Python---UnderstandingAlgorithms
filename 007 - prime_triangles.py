## ----- PRIME TRIANGLE ----
## 
## TASK CONDITIONS:
#  1. Get input number N and create a sequence from 1 to N (inclusive).
#  2. Find out which numbers in the sequence are prime and represent prime numbers as 1, other numbers as 0. (prime numbers are: 1, 2, 3, 5, 7)
#  3. Print a new row for each prime number. Each row ends at the next prime number. (ex: 1, 12, 123, 12345, 1234567)
#  
#  # Expected Output if N = 10:
#  #
#  # 1 
#  # 11
#  # 111
#  # 11101
#  # 1110101


def define_primes(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_triangles(num):
    converted_numbers = []
    for i in range(1, num+1):
        if define_primes(i):
            converted_numbers.append(str(1))
            print(''.join(converted_numbers))
        else:
            converted_numbers.append(str(0))

if __name__=='__main__':
    prime_triangles(10)




### tried to use CONDITIONALS but prime_nums wasn't a correct algorythm
###
# def prime_triangles(n):
#     all_nums = [i for i in range(1, n+1)]
#     prime_nums = [i for i in range(1, n+1) if i%2 != 0 or i == 2] # [or n%i == 1] ?? 
#     converted_list = []

#     for j in all_nums:
#         if j in prime_nums:
#             converted_list.append(str('1'))
#             print(''.join(converted_list))
#         else:
#             converted_list.append(str('0'))