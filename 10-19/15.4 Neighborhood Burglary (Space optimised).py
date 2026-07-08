from typing import List

def neighborhood_burglary(houses: List[int]) -> int:
    # base case
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]

    n = len(houses)
    prev_prev = houses[0]
    prev = max(houses[0], houses[1])

    for i in range(2, n):
        temp = prev
        prev = max(prev, prev_prev + houses[i])
        prev_prev = temp
    return prev