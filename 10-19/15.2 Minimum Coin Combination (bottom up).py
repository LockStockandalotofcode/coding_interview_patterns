from typing import List

def min_coin_combination(coins: List[int], target: int) -> int:
    dp = [float('inf')] * (target + 1)

    if target == 0:
        return 0
    if not coins:
        return -1
    dp[0] = 0

    for t in range(1, target+1):
        for coin in coins:
            if coin <= target:
                dp[t] = min(dp[t], 1 + dp[t - coin])
    
    res = dp[target]

    return -1 if res == float('inf') else res