from typing import List

def hamming_weights_of_integers(n: int) -> List[int]:
    dp = [0] * (n+1)

    for num in range(1, n+1):
        dp[num] = dp[num >> 1] + (num & 1)
        # sum of set bits of last number + LSB of this 
    
    return dp