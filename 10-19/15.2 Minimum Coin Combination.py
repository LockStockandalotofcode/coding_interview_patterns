from typing import List

def min_coin_combination(coins: List[int], target: int) -> int:
    # top down with memoization
    memo = {}
    if target == 0:
        return 0
    if not coins:
        return -1
    
    def dp_helper(target: int) -> int:
        if target == 0:
            return 0
        if target in memo:
            return memo[target]
        # initialise coins to a large positive number
        min_num = float('inf')
        for coin in coins:
            if coin <= target:
                min_num = min(min_num, 1 + dp_helper(target - coin))
        memo[target] = min_num
        return memo[target]

    res = dp_helper(target)
    return -1 if res == float('inf') else res