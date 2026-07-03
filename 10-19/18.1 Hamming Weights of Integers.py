from typing import List

def count_set_bit_helper(x: int) -> int:
    count = 0

    while x > 0:
        # count set bits, traversing LSB, using rightwise shift analogous to incrementing 
        
        count += x & 1
        x >>= 1

    return count

def hamming_weights_of_integers(n: int) -> List[int]:
    return [count_set_bit_helper(i) for i in range(n + 1)]
