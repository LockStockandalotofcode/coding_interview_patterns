from typing import List

def gas_stations(gas: List[int], cost: List[int]) -> int:
    # GREEDY 
    # any starting point in the array that leads to end of array without tank in deficit(negative), implies that solution exists
    # greedy strategy considers the starting point to be solution

    if sum(gas) < sum(cost):
        return -1
    
    # if total gas is more than total cost, a solution must exist
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        # if at any point, tank goes in deficit, reset and start from point where deficit was realised
        if tank < 0:
            start, tank = i + 1, 0
    
    return start