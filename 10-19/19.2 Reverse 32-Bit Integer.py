import math

def reverse_32_bit_integer(n: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = - 2**31

    reversed_n = 0

    while n != 0:
        # digit = n % 10
        digit = int(math.fmod(n, 10))
        # n = n // 10
        n = int(n / 10)

        # conditional check 
        if reversed_n > (INT_MAX // 10) or reversed_n < (INT_MIN // 10):
            return 0
        
        reversed_n = reversed_n * 10 + digit
    
    return reversed_n