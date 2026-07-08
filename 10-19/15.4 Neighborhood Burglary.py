from typing import List

def neighborhood_burglary(houses: List[int]) -> int:
    # base case
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]

    n = len(houses)
    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], houses[i] + dp[i-2])
    
    return dp[n-1]